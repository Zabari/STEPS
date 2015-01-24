from flask import request, jsonify
from flask.ext import restful
import server

#See here: https://flask-restful.readthedocs.org/en/0.3.1/quickstart.html

######## API Resources #########

# /api/escalators/all/status
# /api/escalators/up23/status

# /api/escalators/all/history, same as /api/escalators/all/history?min=0&max=100
# /api/escalators/up23/history

# includes next and previous with different min & max values

# /api/escalators/all/history?min=23&max=25
# /api/escalators/up23/history

MAX_RECORDS_AT_ONCE = 1000

class API(restful.Resource):
    def get(self, escalator, data_type):
        if data_type == None:
            data_type = "status"

        # Used for /history
        min_record = request.args.get("min")
        max_record = request.args.get("max")

        errors = verify_api_parameters(escalator, data_type, min_record, max_record)
        if errors:
            return errors

        # If min and max are set, typecast into int
        if min_record != None and max_record != None:
            min_record = int(min_record)
            max_record = int(max_record)

        if data_type == "history":
            if escalator == "all":
                results = server.fetchHistoryIntervalAll(min_record, max_record)
            else:
                results = server.fetchHistoryInterval(escalator, min_record, max_record)

        # Fetch current status
        else:
            if escalator == "all":
                results = server.fetchHistoryIntervalAll(mini=0, maxi=0)
            else:
                results = server.fetchHistoryInterval(escalator, mini=0, maxi=0)

        return jsonify(**results)


def verify_api_parameters(escalator, data_type, min_record, max_record):
    # Verify data type
    if data_type not in ["history", "status"]:
        return api_error_message("Invalid data_type: Must be empty or 'status' or 'history'")

    # Veryify escalator
    if escalator not in ["all", "up23", "down23","up24", "down24","up35", "down35","up46", "down46","up57", "down57","up68", "down68","up79", "down79"]:
        return api_error_message("Invalid escalator name. Must be 'all' or direction followed by two floors, ex. 'up57'")

    # Verify max & min values (if set)
    if min_record != None and max_record != None:
        if not (min_record.isdigit() and max_record.isdigit()):
            return api_error_message("Malformed max and min values")
        
        min_record = int(min_record)
        max_record = int(max_record)

        if not (max_record >= min_record and max_record >= 0 and min_record >= 0):
            return api_error_message("Malformed max and min values")

    # Parameters are valid
    return None

    
def api_error_message(message):
    return jsonify(error=message)
