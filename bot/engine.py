"""Bot response logic.
Ported from the Java UAAS bot handlers (reference modules) into pure-Python
mock responses. Swap the mock payloads with real REST/gRPC service calls
when wiring up the actual UAAS backend - the UI layer never changes.
"""
from __future__ import annotations
# ---------------------------------------------------------------------------
# Mock responses for sidebar quick actions
# ---------------------------------------------------------------------------
ACTION_RESPONSES: dict[str, str] = {
    "get_user_info": (
        "\U0001F464 **Get user info** completed.\n\n"
        "```json\n"
        "{\n"
        "  \"userId\": \"u-10241\",\n"
        "  \"userName\": \"demo.user\",\n"
        "  \"email\": \"demo.user@acme.com\",\n"
        "  \"status\": \"ACTIVE\"\n"
        "}\n"
        "```"
    ),
    "get_user_status": (
        "✅ **Get user status** completed.\n\n"
        "User `demo.user` is currently **ACTIVE** (last login: today 09:12 UTC)."
    ),
    "reset_user": (
        "♻️ **Reset user** completed.\n\n"
        "MFA devices cleared, sessions revoked, and a temporary password "
        "`Tmp-8f2k!q` was issued (valid for 24 hours)."
    ),
    "modify_user": (
        "✏️ **Modify user** completed.\n\n"
        "Updated attributes: `department -> Platform Ops`."
    ),
    "get_user_audit": (
        "\U0001F9FE **Get user audit** completed.\n\n"
        "- 09:12 - LOGIN SUCCESS (10.66.192.41)\n"
        "- 08:44 - PASSWORD CHANGE\n"
        "- Yesterday - TOKEN REFRESH"
    ),
    "change_password": (
        "\U0001F512 **Change password** completed.\n\n"
        "Password rotated successfully. Next change due in 90 days."
    ),
    "generate_activation_code": (
        "\U0001F511 **Generate activation code** completed.\n\n"
        "Activation code: `ACT-7Q2M-9XZB-4410` (valid for 30 minutes)."
    ),
    "download_activation_package": (
        "\U0001F4E6 **Download activation package** completed.\n\n"
        "`uaas-activation-u10241.zip` (2.4 MB) is ready - check the "
        "notifications panel for the download link."
    ),
    "generate_user_jwt": (
        "\U0001F3AB **Generate user jwt** completed.\n\n"
        "JWT issued for `demo.user`, expires in **60 minutes**. "
        "Token preview: `eyJhbGciOiJIUzI1NiIs...`"
    ),
    "add_service_jwt_key": (
        "\U0001F9E9 **Add service jwt key** completed.\n\n"
        "Key `svc-uaas-2026-01` registered with scope `uaas:read`."
    ),
    "get_group_info": (
        "\U0001F465 **Get group info** completed.\n\n"
        "`grp-platform-admins` - 14 members, 3 service accounts, "
        "owner: `p.moore@acme.com`."
    ),
    "modify_group": (
        "✏️ **Modify group** completed.\n\n"
        "Description updated to `Platform administrators (prod)`."
    ),
    "update_thumbprint_group": (
        "\U0001F6E1️ **Update thumbprint group** completed.\n\n"
        "Thumbprint `9F:2C:AA:...:71D4` added to the group trust store."
    ),
    "send_email": (
        "\U0001F4E7 **Send email** queued.\n\n"
        "To: `demo.user@acme.com` - Your UAAS access request - status: **QUEUED**."
    ),
    "send_sms": (
        "\U0001F4F1 **Send sms** queued.\n\n"
        "To: `+65-****-4321` - verification code sent. Status: **QUEUED**."
    ),
    "check_email": (
        "\U0001F4EC **Check email** completed.\n\n"
        "2 unread messages found (1 activation notice, 1 policy update)."
    ),
}
# Very light natural-language router so free-typed text can hit an action too
_KEYWORD_ROUTES: dict[str, tuple[str, ...]] = {
    "get_user_info": ("user info", "who am i"),
    "get_user_status": ("user status", "am i active"),
    "change_password": ("change password", "reset password"),
    "generate_activation_code": ("activation code",),
    "generate_user_jwt": ("jwt", "token"),
    "send_email": ("send mail", "send email"),
    "send_sms": ("sms", "text message"),
    "check_email": ("check mail", "inbox"),
}
def respond_to_action(action_id: str) -> str:
    """Return the bot reply for a sidebar quick action."""
    return ACTION_RESPONSES.get(
        action_id, f"✅ Action `{action_id}` completed successfully."
    )
def respond_to_text(text: str) -> str:
    """Return the bot reply for a free-typed chat message."""
    lowered = text.strip().lower()
    for action_id, keywords in _KEYWORD_ROUTES.items():
        if any(keyword in lowered for keyword in keywords):
            return respond_to_action(action_id)
    if lowered in {"hi", "hello", "hey"} or "hello" in lowered:
        return (
            "\U0001F44B Hello! How can I help? Pick a **Quick Action** from the "
            "left-hand panel, or type a request."
        )
    if "help" in lowered:
        return (
            "\U0001F9ED I can help with **users, auth/keys, groups and notifications**. "
            "Use the Quick Actions panel on the left to get started."
        )
    return (
        f"\U0001F914 I received: \"{text}\".\n\n"
        "I'm running in demo mode - try a **Quick Action** from the sidebar "
        "for a real operation."
    )
