from .fields import fields
from .base import BaseSchema


class JoinPolicy(BaseSchema):

    label = fields.Label(load_only=True, required=True)
    alice_verifying_key = fields.Key(load_only=True, required=True)
    policy_encrypting_key = fields.Key(dump_only=True)


class Retrieve(BaseSchema):
    label = fields.Label(required=True, load_only=True)
    policy_encrypting_key = fields.Key(required=True, load_only=True)
    alice_verifying_key = fields.Key(required=True, load_only=True, )
    message_kit = fields.MessageKit(required=True, load_only=True)

    cleartexts = fields.List(fields.Str(), dump_only=True)


class PublicKeys(BaseSchema):
    bob_encrypting_key = fields.Key(dump_only=True)
    bob_verifying_key = fields.Key(dump_only=True)


specifications = {'join_policy': JoinPolicy(),
                    'retrieve': Retrieve(),
                    'public_keys': PublicKeys()}