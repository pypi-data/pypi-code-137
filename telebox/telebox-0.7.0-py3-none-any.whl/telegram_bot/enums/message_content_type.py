from enum import Enum


class MessageContentType(Enum):
    TEXT = "text"
    ANIMATION = "animation"
    AUDIO = "audio"
    DOCUMENT = "document"
    PHOTO = "photo"
    STICKER = "sticker"
    VIDEO = "video"
    VIDEO_NOTE = "video_note"
    VOICE = "voice"
    CONTACT = "contact"
    DICE = "dice"
    GAME = "game"
    POLL = "poll"
    VENUE = "venue"
    LOCATION = "location"
    NEW_CHAT_MEMBERS = "new_chat_members"
    LEFT_CHAT_MEMBER = "left_chat_member"
    NEW_CHAT_TITLE = "new_chat_title"
    NEW_CHAT_PHOTO = "new_chat_photo"
    DELETE_CHAT_PHOTO = "delete_chat_photo"
    GROUP_CHAT_CREATED = "group_chat_created"
    SUPERGROUP_CHAT_CREATED = "supergroup_chat_created"
    CHANNEL_CHAT_CREATED = "channel_chat_created"
    MESSAGE_AUTO_DELETE_TIMER_CHANGED = "message_auto_delete_timer_changed"
    MIGRATE_TO_CHAT_ID = "migrate_to_chat_id"
    MIGRATE_FROM_CHAT_ID = "migrate_from_chat_id"
    PINNED_MESSAGE = "pinned_message"
    INVOICE = "invoice"
    SUCCESSFUL_PAYMENT = "successful_payment"
    CONNECTED_WEBSITE = "connected_website"
    PASSPORT_DATA = "passport_data"
    PROXIMITY_ALERT_TRIGGERED = "proximity_alert_triggered"
    VIDEO_CHAT_SCHEDULED = "video_chat_scheduled"
    VIDEO_CHAT_STARTED = "video_chat_started"
    VIDEO_CHAT_ENDED = "video_chat_ended"
    VIDEO_CHAT_PARTICIPANTS_INVITED = "video_chat_participants_invited"
    WEB_APP_DATA = "web_app_data"
