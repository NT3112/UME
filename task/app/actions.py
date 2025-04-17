
ACTIONS = {
    "ORDER_FOOD": "Order Food Online",
    "FIND_RECIPE": "Find Pizza Recipes",
    "ASK_HELP": "Ask for Help",
    "SHARE_NEWS": "Share News Update",
    "SLEEP":"Go to Sleep",
    
}

def suggest_actions(intent):
    suggestions = []

    if intent == "Order Food":
        suggestions.append({"action_code": "ORDER_FOOD", "display_text": ACTIONS["ORDER_FOOD"]})
        suggestions.append({"action_code": "FIND_RECIPE", "display_text": ACTIONS["FIND_RECIPE"]})
    elif intent == "Ask Question":
        suggestions.append({"action_code": "ASK_HELP", "display_text": ACTIONS["ASK_HELP"]})
    else:
        suggestions.append({"action_code": "SHARE_NEWS", "display_text": ACTIONS["SHARE_NEWS"]})

    return suggestions[:3]
