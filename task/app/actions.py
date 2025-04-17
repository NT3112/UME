
ACTIONS = {
    "ORDER_FOOD": "Order food online",
    
    "FIND_REST":"Find the needed restaurants",
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
        suggestions.append({"action": intent, "display": "Provide the necessary food options"})
        suggestions.append({"action": intent, "display": "Get the required list of restaurants"})

    elif intent == "ASK_HELP":
        suggestions.append({"action": intent, "display": ACTIONS[intent]})
        suggestions.append({"action": intent, "display": "What kind of help"})
        suggestions.append({"action": intent, "display": "Provide the necessary help"})
        
    elif intent=="SET_REMINDER":
        suggestions.append({"action": intent, "display": ACTIONS[intent]})
        suggestions.append({"action": intent, "display": "Set an alarm for the required time"})
        suggestions.append({"action": intent, "display": "Restart on snoozebutton"})
    elif intent=="SHARE_NEWS":
        suggestions.append({"action": intent, "display": ACTIONS[intent]})
        suggestions.append({"action": intent, "display": "Type of  news to be shown "})
        suggestions.append({"action": "SHARE_NEWS", "display": "Category for each news"})

    else:
        suggestions.append({"action": intent, "display": "Vague Request"})


    return suggestions[:3]

