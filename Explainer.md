
# 1. State Machine

The state machine is implemented in `state_machine.py`:

```
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
```

Illegal transitions are prevented by validating against this dictionary.

---

# 2. File Upload

Validation is handled in serializer:

```
def validate_file(self, file):
    if file.size > 5 * 1024 * 1024:
        raise serializers.ValidationError("File too large")

    if not file.name.endswith(('.pdf','.jpg','.png')):
        raise serializers.ValidationError("Invalid file type")

    return file
```

If a 50MB file is uploaded, it is rejected with a validation error.

---

# 3. Queue

Query:

```
KYCSubmission.objects.filter(state='submitted').order_by('created_at')
```

SLA:

```
(now() - created_at) > 24 hours
```

This is computed dynamically to avoid stale data.

---

# 4. Auth

Merchants are restricted to their own data:

```
if user.role == 'merchant':
    return KYCSubmission.objects.filter(user=user)
```

Reviewers can see all submissions.

---

# 5. AI Audit

AI initially suggested directly updating state:

```
submission.state = new_state
submission.save()
```

This was insecure because it allowed invalid transitions.

I replaced it with a centralized state machine to enforce strict rules.
