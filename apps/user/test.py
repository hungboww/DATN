import logging
import os

from django.conf import settings
from pubnub.models.consumer.v3.channel import Channel
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.exceptions import PubNubException

from .models import CreateUserModel

logger = logging.getLogger(__name__)

pnconfig = PNConfiguration()

pnconfig.publish_key = 'pub-c-291fa83f-9f91-405c-92b0-c68f88d49a00'
pnconfig.subscribe_key = 'sub-c-113d9d1a-4f8d-40e0-a3d1-7a8e7f471f3a'
pnconfig.secret_key = 'sec-c-OTBlYzNjZjgtYzAwYy00ZDAyLTk0ZTEtZjI4NmQ1ZWQzZGY2'
pnconfig.user_id = '92b0'
pnconfig.ssl = True

pubnub = PubNub(pnconfig)

class PubNubService:
    DEFAULT_NOTIFICATION_TTL = 60  # 60 minutes
    @staticmethod
    def get_notification_token_for_user(user: CreateUserModel, ttl: int = DEFAULT_NOTIFICATION_TTL):
        envalope = pubnub.grant_token() \
            .channels([Channel.id(user.get_notification_channel_name()).read().delete()]) \
            .ttl(ttl) \
            .authorized_uuid(user.get_notification_channel_name()) \
            .sync()
        print("envalope", envalope.result)
        token = envalope.result.token
        token_payload = pubnub.parse_token(token)

        return {
            "exp_timestamp": token_payload["timestamp"],
            "token": token,
            "ttl": token_payload["ttl"],
        }

    @staticmethod
    def send_notification_to_user(user: CreateUserModel, message):
        try:
            pubnub.publish() \
                .channel(user.get_notification_channel_name()) \
                .message(message) \
                .use_post(use_post=True) \
                .sync()
        except PubNubException as e:
            logger.error(e)
