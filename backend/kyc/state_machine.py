VALID_TRANSITIONS = {
    "draft": ["submitted"],
    "submitted": ["under_review"],
    "under_review": ["approved", "rejected", "more_info_requested"],
    "more_info_requested": ["submitted"]
}

def change_state(submission, new_state):
    if new_state not in VALID_TRANSITIONS.get(submission.state, []):
        raise Exception("Invalid transition")

    submission.state = new_state
    submission.save()