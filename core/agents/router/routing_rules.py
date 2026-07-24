ROUTING_RULES = {

    "finance": [
        "Finance Agent"
    ],

    "wealth": [
        "Finance Agent"
    ],

    "investment": [
        "Finance Agent"
    ],


    "insurance": [
        "Insurance Agent"
    ],

    "policy": [
        "Insurance Agent"
    ],

    "advisor": [
        "Insurance Agent",
        "Marketing Agent"
    ],


    "content": [
        "Content Agent"
    ],

    "video": [
        "Video Agent"
    ],

    "marketing": [
        "Marketing Agent"
    ],


    "technology": [
        "CTO Agent"
    ],

    "software": [
        "CTO Agent"
    ],


    "business": [
        "CEO Agent"
    ],

    "strategy": [
        "CEO Agent"
    ]
}


def find_agents(task):

    task = task.lower()

    selected = []

    for keyword, agents in ROUTING_RULES.items():

        if keyword in task:

            for agent in agents:

                if agent not in selected:
                    selected.append(agent)


    if not selected:
        selected.append("CEO Agent")


    return selected