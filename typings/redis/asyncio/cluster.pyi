"""
This type stub file was generated by pyright.
"""

from _typeshed import Incomplete
from collections.abc import Awaitable, Callable, Mapping
from types import TracebackType
from typing import Any, Generic
from typing_extensions import Self
from redis.asyncio.client import ResponseCallbackT
from redis.asyncio.connection import BaseParser, Connection, Encoder
from redis.asyncio.parser import CommandsParser
from redis.client import AbstractRedis
from redis.cluster import AbstractRedisCluster, LoadBalancer
from redis.commands.core import _StrType
from redis.credentials import CredentialProvider
from redis.retry import Retry
from redis.typing import AnyKeyT, EncodableT, KeyT

class ClusterParser(BaseParser):
    ...


class RedisCluster(AbstractRedis, AbstractRedisCluster, Generic[_StrType]):
    retry: Retry | None
    connection_kwargs: dict[str, Any]
    nodes_manager: NodesManager
    encoder: Encoder
    read_from_replicas: bool
    reinitialize_steps: int
    cluster_error_retry_attempts: int
    reinitialize_counter: int
    commands_parser: CommandsParser
    node_flags: set[str]
    command_flags: dict[str, str]
    response_callbacks: Incomplete
    result_callbacks: dict[str, Callable[[Incomplete, Incomplete], Incomplete]]
    def __init__(self, host: str | None = ..., port: str | int = ..., startup_nodes: list[ClusterNode] | None = ..., require_full_coverage: bool = ..., read_from_replicas: bool = ..., reinitialize_steps: int = ..., cluster_error_retry_attempts: int = ..., connection_error_retry_attempts: int = ..., max_connections: int = ..., db: str | int = ..., path: str | None = ..., credential_provider: CredentialProvider | None = ..., username: str | None = ..., password: str | None = ..., client_name: str | None = ..., encoding: str = ..., encoding_errors: str = ..., decode_responses: bool = ..., health_check_interval: float = ..., socket_connect_timeout: float | None = ..., socket_keepalive: bool = ..., socket_keepalive_options: Mapping[int, int | bytes] | None = ..., socket_timeout: float | None = ..., retry: Retry | None = ..., retry_on_error: list[Exception] | None = ..., ssl: bool = ..., ssl_ca_certs: str | None = ..., ssl_ca_data: str | None = ..., ssl_cert_reqs: str = ..., ssl_certfile: str | None = ..., ssl_check_hostname: bool = ..., ssl_keyfile: str | None = ..., address_remap: Callable[[str, int], tuple[str, int]] | None = ...) -> None:
        ...
    
    async def initialize(self) -> Self:
        ...
    
    async def close(self) -> None:
        ...
    
    async def __aenter__(self) -> Self:
        ...
    
    async def __aexit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None:
        ...
    
    def __await__(self) -> Awaitable[Self]:
        ...
    
    def __del__(self) -> None:
        ...
    
    async def on_connect(self, connection: Connection) -> None:
        ...
    
    def get_nodes(self) -> list[ClusterNode]:
        ...
    
    def get_primaries(self) -> list[ClusterNode]:
        ...
    
    def get_replicas(self) -> list[ClusterNode]:
        ...
    
    def get_random_node(self) -> ClusterNode:
        ...
    
    def get_default_node(self) -> ClusterNode:
        ...
    
    def set_default_node(self, node: ClusterNode) -> None:
        ...
    
    def get_node(self, host: str | None = ..., port: int | None = ..., node_name: str | None = ...) -> ClusterNode | None:
        ...
    
    def get_node_from_key(self, key: str, replica: bool = ...) -> ClusterNode | None:
        ...
    
    def keyslot(self, key: EncodableT) -> int:
        ...
    
    def get_encoder(self) -> Encoder:
        ...
    
    def get_connection_kwargs(self) -> dict[str, Any | None]:
        ...
    
    def set_response_callback(self, command: str, callback: ResponseCallbackT) -> None:
        ...
    
    async def execute_command(self, *args: EncodableT, **kwargs: Any) -> Any:
        ...
    
    def pipeline(self, transaction: Any | None = ..., shard_hint: Any | None = ...) -> ClusterPipeline[_StrType]:
        ...
    
    @classmethod
    def from_url(cls, url: str, **kwargs) -> Self:
        ...
    


class ClusterNode:
    host: str
    port: str | int
    name: str
    server_type: str | None
    max_connections: int
    connection_class: type[Connection]
    connection_kwargs: dict[str, Any]
    response_callbacks: dict[Incomplete, Incomplete]
    def __init__(self, host: str, port: str | int, server_type: str | None = ..., *, max_connections: int = ..., connection_class: type[Connection] = ..., **connection_kwargs: Any) -> None:
        ...
    
    def __eq__(self, obj: object) -> bool:
        ...
    
    def __del__(self) -> None:
        ...
    
    async def disconnect(self) -> None:
        ...
    
    def acquire_connection(self) -> Connection:
        ...
    
    async def parse_response(self, connection: Connection, command: str, **kwargs: Any) -> Any:
        ...
    
    async def execute_command(self, *args: Any, **kwargs: Any) -> Any:
        ...
    
    async def execute_pipeline(self, commands: list[PipelineCommand]) -> bool:
        ...
    


class NodesManager:
    startup_nodes: dict[str, ClusterNode]
    require_full_coverage: bool
    connection_kwargs: dict[str, Any]
    default_node: ClusterNode | None
    nodes_cache: dict[str, ClusterNode]
    slots_cache: dict[int, list[ClusterNode]]
    read_load_balancer: LoadBalancer
    address_remap: Callable[[str, int], tuple[str, int]] | None
    def __init__(self, startup_nodes: list[ClusterNode], require_full_coverage: bool, connection_kwargs: dict[str, Any], address_remap: Callable[[str, int], tuple[str, int]] | None = ...) -> None:
        ...
    
    def get_node(self, host: str | None = ..., port: int | None = ..., node_name: str | None = ...) -> ClusterNode | None:
        ...
    
    def set_nodes(self, old: dict[str, ClusterNode], new: dict[str, ClusterNode], remove_old: bool = ...) -> None:
        ...
    
    def get_node_from_slot(self, slot: int, read_from_replicas: bool = ...) -> ClusterNode:
        ...
    
    def get_nodes_by_server_type(self, server_type: str) -> list[ClusterNode]:
        ...
    
    async def initialize(self) -> None:
        ...
    
    async def close(self, attr: str = ...) -> None:
        ...
    
    def remap_host_port(self, host: str, port: int) -> tuple[str, int]:
        ...
    


class ClusterPipeline(AbstractRedis, AbstractRedisCluster, Generic[_StrType]):
    def __init__(self, client: RedisCluster[_StrType]) -> None:
        ...
    
    async def initialize(self) -> Self:
        ...
    
    async def __aenter__(self) -> Self:
        ...
    
    async def __aexit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None:
        ...
    
    def __await__(self) -> Awaitable[Self]:
        ...
    
    def __enter__(self) -> Self:
        ...
    
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None:
        ...
    
    def __bool__(self) -> bool:
        ...
    
    def __len__(self) -> int:
        ...
    
    def execute_command(self, *args: KeyT | EncodableT, **kwargs: Any) -> Self:
        ...
    
    async def execute(self, raise_on_error: bool = ..., allow_redirections: bool = ...) -> list[Any]:
        ...
    
    def mset_nonatomic(self, mapping: Mapping[AnyKeyT, EncodableT]) -> Self:
        ...
    


class PipelineCommand:
    args: Any
    kwargs: Any
    position: int
    result: Exception | None | Any
    def __init__(self, position: int, *args: Any, **kwargs: Any) -> None:
        ...
    


