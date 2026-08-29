"""Application-wide constants: branding, texts and the Quick Actions tree."""
from __future__ import annotations
APP_NAME = "UAAS Chatbot"
SIDEBAR_HEADER = "Quick Actions"
WELCOME_BODY = "Choose an action from the left-hand panel to get started."
CHAT_PLACEHOLDER = "Type a message..."
# Quick-action groups rendered in the sidebar (id is routed to bot/engine.py)
ACTION_GROUPS: list[dict] = [
    {
        "id": "user",
        "title": "User",
        "icon": "\U0001F464",
        "actions": [
            {"id": "get_user_info", "label": "Get user info"},
            {"id": "get_user_status", "label": "Get user status"},
            {"id": "reset_user", "label": "Reset user"},
            {"id": "modify_user", "label": "Modify user"},
            {"id": "get_user_audit", "label": "Get user audit"},
            {"id": "change_password", "label": "Change password"},
        ],
    },
    {
        "id": "auth",
        "title": "Auth / Keys",
        "icon": "\U0001F511",
        "actions": [
            {"id": "generate_activation_code", "label": "Generate activation code"},
            {"id": "download_activation_package", "label": "Download activation package"},
            {"id": "generate_user_jwt", "label": "Generate user jwt"},
            {"id": "add_service_jwt_key", "label": "Add service jwt key"},
        ],
    },
    {
        "id": "group",
        "title": "Group",
        "icon": "\U0001F465",
        "actions": [
            {"id": "get_group_info", "label": "Get group info"},
            {"id": "modify_group", "label": "Modify group"},
            {"id": "update_thumbprint_group", "label": "Update thumbprint group"},
        ],
    },
    {
        "id": "notifications",
        "title": "Notifications",
        "icon": "\U0001F514",
        "actions": [
            {"id": "send_email", "label": "Send email"},
            {"id": "send_sms", "label": "Send sms"},
            {"id": "check_email", "label": "Check email"},
        ],
    },
]
