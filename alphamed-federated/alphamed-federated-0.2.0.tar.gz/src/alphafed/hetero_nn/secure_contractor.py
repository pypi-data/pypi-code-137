"""HeteroNN contractor."""

import secrets
from dataclasses import dataclass
from typing import List

from ..contractor import (ApplySendingDataEvent, ContractEvent,
                          TaskMessageContractor)
from .psi.rsa_psi_contractor import RSAContractor, RSAEventFactory


@dataclass
class CheckinEvent(ContractEvent):
    """An event of checkin for a specific task."""

    TYPE = 'checkin'

    peer_id: str
    nonce: str

    @classmethod
    def contract_to_event(cls, contract: dict) -> 'CheckinEvent':
        event_type = contract.get('type')
        peer_id = contract.get('peer_id')
        nonce = contract.get('nonce')
        assert event_type == cls.TYPE, f'合约类型错误: {event_type}'
        assert peer_id and isinstance(peer_id, str), f'invalid peer_id: {peer_id}'
        assert nonce or isinstance(nonce, str), f'invalid nonce: {nonce}'
        return CheckinEvent(peer_id=peer_id, nonce=nonce)


@dataclass
class CheckinResponseEvent(ContractEvent):
    """An event of responding checkin event."""

    TYPE = 'checkin_response'

    round: int
    host: str
    nonce: str

    @classmethod
    def contract_to_event(cls, contract: dict) -> 'CheckinResponseEvent':
        event_type = contract.get('type')
        round = contract.get('round')
        host = contract.get('host')
        nonce = contract.get('nonce')
        assert event_type == cls.TYPE, f'合约类型错误: {event_type}'
        assert isinstance(round, int) and round >= 0, f'invalid round: {round}'
        assert host and isinstance(host, str), f'invalid host: {host}'
        assert nonce and isinstance(nonce, str), f'invalid nonce: {nonce}'
        return CheckinResponseEvent(round=round, host=host, nonce=nonce)


@dataclass
class CheckinACKEvent(ContractEvent):
    """An event of checkin event ACK response."""

    TYPE = 'checkin_ack'

    peer_id: str

    @classmethod
    def contract_to_event(cls, contract: dict) -> 'CheckinACKEvent':
        event_type = contract.get('type')
        round = contract.get('round')
        host = contract.get('host')
        nonce = contract.get('nonce')
        assert event_type == cls.TYPE, f'合约类型错误: {event_type}'
        assert isinstance(round, int) and round >= 0, f'invalid round: {round}'
        assert host and isinstance(host, str), f'invalid host: {host}'
        assert nonce and isinstance(nonce, str), f'invalid nonce: {nonce}'
        return CheckinResponseEvent(round=round, host=host, nonce=nonce)


@dataclass
class SyncStateEvent(ContractEvent):
    """An event of synchronising task state."""

    TYPE = 'sync_state'

    round: int
    host: str

    @classmethod
    def contract_to_event(cls, contract: dict) -> 'SyncStateEvent':
        event_type = contract.get('type')
        round = contract.get('round')
        host = contract.get('host')
        assert event_type == cls.TYPE, f'合约类型错误: {event_type}'
        assert isinstance(round, int) and round >= 0, f'invalid round: {round}'
        assert host and isinstance(host, str), f'invalid host: {host}'
        return SyncStateEvent(round=round, host=host)


@dataclass
class SyncStateResponseEvent(ContractEvent):
    """An event of responding to synchronising task state event."""

    TYPE = 'sync_state_response'

    round: int
    peer_id: str

    @classmethod
    def contract_to_event(cls, contract: dict) -> 'SyncStateResponseEvent':
        event_type = contract.get('type')
        round = contract.get('round')
        peer_id = contract.get('peer_id')
        assert event_type == cls.TYPE, f'合约类型错误: {event_type}'
        assert isinstance(round, int) and round >= 0, f'invalid round: {round}'
        assert peer_id and isinstance(peer_id, str), f'invalid peer_id: {peer_id}'
        return SyncStateResponseEvent(round=round, peer_id=peer_id)


@dataclass
class StartRoundEvent(ContractEvent):
    """An event of starting a new round of training."""

    TYPE = 'start_round'

    round: int

    @classmethod
    def contract_to_event(cls, contract: dict) -> 'StartRoundEvent':
        event_type = contract.get('type')
        round = contract.get('round')
        assert event_type == cls.TYPE, f'合约类型错误: {event_type}'
        assert isinstance(round, int) and round > 0, f'invalid round: {round}'
        return StartRoundEvent(round=round)


@dataclass
class ReadyForFusionEvent(ContractEvent):
    """An event of notifying that the host is ready for receiving cipher features."""

    TYPE = 'ready_4_fusion'

    round: int

    @classmethod
    def contract_to_event(cls, contract: dict) -> 'ReadyForFusionEvent':
        event_type = contract.get('type')
        round = contract.get('round')
        assert event_type == cls.TYPE, f'合约类型错误: {event_type}'
        assert isinstance(round, int) and round > 0, f'invalid round: {round}'
        return ReadyForFusionEvent(round=round)


@dataclass
class ReadyForNoisedProjectionEvent(ContractEvent):
    """An event of notifying that the host is ready for collecting noised features projection."""

    TYPE = 'ready_4_proj'

    round: int

    @classmethod
    def contract_to_event(cls, contract: dict) -> 'ReadyForNoisedProjectionEvent':
        event_type = contract.get('type')
        round = contract.get('round')
        assert event_type == cls.TYPE, f'合约类型错误: {event_type}'
        assert isinstance(round, int) and round > 0, f'invalid round: {round}'
        return ReadyForNoisedProjectionEvent(round=round)


@dataclass
class ReadyForNoisedWGradEvent(ContractEvent):
    """An event of notifying that the host is ready for collecting noised W grad of project layer."""

    TYPE = 'ready_4_w_grad'

    round: int

    @classmethod
    def contract_to_event(cls, contract: dict) -> 'ReadyForNoisedWGradEvent':
        event_type = contract.get('type')
        round = contract.get('round')
        assert event_type == cls.TYPE, f'合约类型错误: {event_type}'
        assert isinstance(round, int) and round > 0, f'invalid round: {round}'
        return ReadyForNoisedWGradEvent(round=round)


@dataclass
class CloseRoundEvent(ContractEvent):
    """An event of closing a specific round of training."""

    TYPE = 'close_round'

    round: int

    @classmethod
    def contract_to_event(cls, contract: dict) -> 'CloseRoundEvent':
        event_type = contract.get('type')
        round = contract.get('round')
        assert event_type == cls.TYPE, f'合约类型错误: {event_type}'
        assert isinstance(round, int) and round > 0, f'invalid round: {round}'
        return CloseRoundEvent(round=round)


@dataclass
class StartTestRoundEvent(ContractEvent):
    """An event of starting a new round of testing."""

    TYPE = 'start_test_round'

    round: int

    @classmethod
    def contract_to_event(cls, contract: dict) -> 'StartTestRoundEvent':
        event_type = contract.get('type')
        round = contract.get('round')
        assert event_type == cls.TYPE, f'合约类型错误: {event_type}'
        assert isinstance(round, int) and round > 0, f'invalid round: {round}'
        return StartTestRoundEvent(round=round)


@dataclass
class CloseTestRoundEvent(ContractEvent):
    """An event of closing a round of testing."""

    TYPE = 'close_test_round'

    round: int

    @classmethod
    def contract_to_event(cls, contract: dict) -> 'CloseTestRoundEvent':
        event_type = contract.get('type')
        round = contract.get('round')
        assert event_type == cls.TYPE, f'合约类型错误: {event_type}'
        assert isinstance(round, int) and round > 0, f'invalid round: {round}'
        return CloseTestRoundEvent(round=round)


@dataclass
class CollaboratorCompleteEvent(ContractEvent):
    """An event of notify a collaborator completes its task."""

    TYPE = 'collab_complete'

    peer_id: str

    @classmethod
    def contract_to_event(cls, contract: dict) -> 'CompleteTaskEvent':
        event_type = contract.get('type')
        peer_id = contract.get('peer_id')
        assert event_type == cls.TYPE, f'合约类型错误: {event_type}'
        assert peer_id and isinstance(peer_id, str), f'invalid peer_id: {peer_id}'
        return CollaboratorCompleteEvent(peer_id=peer_id)


@dataclass
class FailTaskEvent(ContractEvent):
    """An event of fail the task."""

    TYPE = 'fail_task'

    @classmethod
    def contract_to_event(cls, contract: dict) -> 'FailTaskEvent':
        event_type = contract.get('type')
        assert event_type == cls.TYPE, f'合约类型错误: {event_type}'
        return FailTaskEvent()


@dataclass
class CompleteTaskEvent(ContractEvent):
    """An event of successfully finishing the task."""

    TYPE = 'complete_task'

    @classmethod
    def contract_to_event(cls, contract: dict) -> 'CompleteTaskEvent':
        event_type = contract.get('type')
        assert event_type == cls.TYPE, f'合约类型错误: {event_type}'
        return CompleteTaskEvent()


# define some more friendly alias
SendFeatureEvent = ApplySendingDataEvent
SendCipherPorjectionEvent = ApplySendingDataEvent
SendNoisedPorjectionEvent = ApplySendingDataEvent
SendCipherWGradEvent = ApplySendingDataEvent
SendNoisedWGradEvent = ApplySendingDataEvent
SendCipherFeatureGradEvent = ApplySendingDataEvent
SendTestFeatureEvent = ApplySendingDataEvent


class HeteroNNEventFactory(RSAEventFactory):

    _CLASS_MAP = {
        CheckinEvent.TYPE: CheckinEvent,
        CheckinResponseEvent.TYPE: CheckinResponseEvent,
        SyncStateEvent.TYPE: SyncStateEvent,
        SyncStateResponseEvent.TYPE: SyncStateResponseEvent,
        StartRoundEvent.TYPE: StartRoundEvent,
        ReadyForFusionEvent.TYPE: ReadyForFusionEvent,
        ReadyForNoisedProjectionEvent.TYPE: ReadyForNoisedProjectionEvent,
        ReadyForNoisedWGradEvent.TYPE: ReadyForNoisedWGradEvent,
        CloseRoundEvent.TYPE: CloseRoundEvent,
        StartTestRoundEvent.TYPE: StartTestRoundEvent,
        CloseTestRoundEvent.TYPE: CloseTestRoundEvent,
        CollaboratorCompleteEvent.TYPE: CollaboratorCompleteEvent,
        FailTaskEvent.TYPE: FailTaskEvent,
        CompleteTaskEvent.TYPE: CompleteTaskEvent,
        **RSAEventFactory._CLASS_MAP,
    }


class HeteroNNContractor(RSAContractor):

    def __init__(self, task_id: str):
        super().__init__(task_id=task_id)
        self._event_factory = HeteroNNEventFactory

    def query_partners(self) -> List[str]:
        """Query all partners in the task."""
        return self._task_contractor.query_nodes()

    def checkin(self, peer_id: str) -> str:
        """Checkin to the task.

        :return
            A nonce string used for identifying matched sync_state reply.
        """
        nonce = secrets.token_hex(16)
        event = CheckinEvent(peer_id=peer_id, nonce=nonce)
        self._new_contract(targets=self.EVERYONE, event=event)
        return nonce

    def respond_checkin(self,
                        round: int,
                        host: str,
                        nonce: str,
                        requester_id: str):
        """Respond checkin event."""
        event = CheckinResponseEvent(round=round, host=host, nonce=nonce)
        self._new_contract(targets=[requester_id], event=event)

    def sync_state(self,
                   round: int,
                   host: str,
                   targets: str = TaskMessageContractor.EVERYONE):
        """Help for synchronising task state."""
        event = SyncStateEvent(round=round, host=host)
        self._new_contract(targets=targets, event=event)

    def respond_sync_state(self, round: int, peer_id: str, host: str):
        """Help for synchronising task state."""
        event = SyncStateResponseEvent(round=round, peer_id=peer_id)
        self._new_contract(targets=[host], event=event)

    def start_round(self, round: int):
        """Create a round of training."""
        event = StartRoundEvent(round=round)
        self._new_contract(targets=self.EVERYONE, event=event)

    def notify_ready_for_fusion(self, round: int):
        """Notify all that the host is ready for receiving cipher features."""
        event = ReadyForFusionEvent(round=round)
        self._new_contract(targets=self.EVERYONE, event=event)

    def notify_ready_for_noised_projection(self, round: int):
        """Notify all that the host is ready for collecting noised features projeciton."""
        event = ReadyForNoisedProjectionEvent(round=round)
        self._new_contract(targets=self.EVERYONE, event=event)

    def notify_ready_for_noised_w_grad(self, round: int):
        """Notify all that the host is ready for collecting noised W grad of project layer."""
        event = ReadyForNoisedWGradEvent(round=round)
        self._new_contract(targets=self.EVERYONE, event=event)

    def close_round(self, round: int):
        """Start a round of training."""
        event = CloseRoundEvent(round=round)
        self._new_contract(targets=self.EVERYONE, event=event)

    def start_test_round(self, round: int):
        """Start a round of testing."""
        event = StartTestRoundEvent(round=round)
        self._new_contract(targets=self.EVERYONE, event=event)

    def notify_collaborator_complete(self, peer_id: str, host: str):
        """Notify the host a collaborator completes its task."""
        event = CollaboratorCompleteEvent(peer_id=peer_id)
        self._new_contract(targets=[host], event=event)

    def close_test_round(self, round: int):
        """Start a round of testing."""
        event = CloseTestRoundEvent(round=round)
        self._new_contract(targets=self.EVERYONE, event=event)

    def finish_task(self, is_succ: bool):
        """Finish the specified task."""
        event = CompleteTaskEvent() if is_succ else FailTaskEvent()
        self._new_contract(targets=self.EVERYONE, event=event)
