
ACTIONS = {
    "ORDER_FOOD": "Order food online",
    "FIND_RECIPE": "Find multiple recipes",
    "ASK_HELP": "Ask for help",
    "SET_REMINDER":"Open Clock App",
    "SET_TIME":"Set an alarm for the required time",
    "SHARE_NEWS": "Share News Update",
    "SLEEP":"Go to Sleep",
    
}

def suggest_actions(intent):
    suggestions = []

    if intent == "ORDER_FOOD":
        suggestions.append({"action": intent, "display": ACTIONS[intent]})
        suggestions.append({"action": intent, "display": ACTIONS["FIND_RECIPE"]})
    elif intent == "ASK_HELP":
        suggestions.append({"action": intent, "display": ACTIONS["ASK_HELP"]})
        
    elif intent=="SET_REMINDER":
        suggestions.append({"action": intent, "display": ACTIONS[intent]})
        suggestions.append({"action": intent, "display": ACTIONS["SET_TIME"]})
    elif intent=="SHARE_NEWS":
        suggestions.append({"action": "SHARE_NEWS", "display": ACTIONS["SHARE_NEWS"]})
    else:
        suggestions.append({"action": intent, "display": "Vague Request"})


    return suggestions[:3]

