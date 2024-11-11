# -*- coding:utf-8 -*-
"""
@Author   : g1879
@Contact  : g1879@qq.com
@Copyright: (c) 2024 by g1879, Inc. All Rights Reserved.
@License  : BSD 3-Clause.
"""
from queue import Queue
from typing import Union, List, Iterable, Optional, Literal, Any

from requests.structures import CaseInsensitiveDict

from .._base.driver import Driver
from .._pages.chromium_base import ChromiumBase
from .._pages.chromium_frame import ChromiumFrame

__RES_TYPE__ = Literal['Document', 'Stylesheet', 'Image', 'Media', 'Font', 'Script', 'TextTrack', 'XHR', 'Fetch',
'Prefetch', 'EventSource', 'WebSocket', 'Manifest', 'SignedExchange', 'Ping', 'CSPViolationReport', 'Preflight', 'Other']


class Listener(object):
    _owner: ChromiumBase = ...
    _address: str = ...
    _target_id: str = ...
    _targets: Union[str, dict, True, None] = ...
    _method: Union[set, True] = ...
    _res_type: Union[set, True] = ...
    _caught: Optional[Queue] = ...
    _is_regex: bool = ...
    _driver: Optional[Driver] = ...
    _request_ids: Optional[dict] = ...
    _extra_info_ids: Optional[dict] = ...
    _running_requests: int = ...
    _running_targets: int = ...
    listening: bool = ...

    def __init__(self, owner: ChromiumBase):
        """
        :param owner: 页面对象
        """
        ...

    @property
    def targets(self) -> Optional[set]: ...

    def set_targets(self,
                    targets: Union[str, list, tuple, set, bool, None] = True,
                    is_regex: Optional[bool] = False,
                    method: Union[str, list, tuple, set, bool, None] = ('GET', 'POST'),
                    res_type: Union[__RES_TYPE__, list, tuple, set, bool, None] = True) -> None:
        """指定要等待的数据包
        :param targets: 要匹配的数据包url特征，可用list等传入多个，为True时获取所有
        :param is_regex: 设置的target是否正则表达式
        :param method: 设置监听的请求类型，可指定多个，为True时监听全部
        :param res_type: 设置监听的资源类型，可指定多个，为True时监听全部，可指定的值有：
        Document, Stylesheet, Image, Media, Font, Script, TextTrack, XHR, Fetch, Prefetch, EventSource, WebSocket,
        Manifest, SignedExchange, Ping, CSPViolationReport, Preflight, Other
        :return: None
        """
        ...

    def start(self,
              targets: Union[str, list, tuple, set, bool, None] = None,
              is_regex: Optional[bool] = None,
              method: Union[str, list, tuple, set, bool, None] = None,
              res_type: Union[__RES_TYPE__, list, tuple, set, bool, None] = None) -> None:
        """拦截目标请求，每次拦截前清空结果
        :param targets: 要匹配的数据包url特征，可用list等传入多个，为True时获取所有
        :param is_regex: 设置的target是否正则表达式，为None时保持原来设置
        :param method: 设置监听的请求类型，可指定多个，默认('GET', 'POST')，为True时监听全部，为None时保持原来设置
        :param res_type: 设置监听的资源类型，可指定多个，默认为True时监听全部，为None时保持原来设置，可指定的值有：
        Document, Stylesheet, Image, Media, Font, Script, TextTrack, XHR, Fetch, Prefetch, EventSource, WebSocket,
        Manifest, SignedExchange, Ping, CSPViolationReport, Preflight, Other
        :return: None
        """
        ...

    def wait(self,
             count: int = 1,
             timeout: float = None,
             fit_count: bool = True,
             raise_err: bool = None) -> Union[List[DataPacket], DataPacket, None]:
        """等待符合要求的数据包到达指定数量
        :param count: 需要捕捉的数据包数量
        :param timeout: 超时时间（秒），为None无限等待
        :param fit_count: 是否必须满足总数要求，发生超时，为True返回False，为False返回已捕捉到的数据包
        :param raise_err: 超时时是否抛出错误，为None时根据Settings设置
        :return: count为1时返回数据包对象，大于1时返回列表，超时且fit_count为True时返回False
        """
        ...

    def steps(self,
              count: int = None,
              timeout: float = None,
              gap=1) -> Iterable[Union[DataPacket, List[DataPacket]]]:
        """用于单步操作，可实现每收到若干个数据包执行一步操作（如翻页）
        :param count: 需捕获的数据包总数，为None表示无限
        :param timeout: 每个数据包等待时间（秒），为None表示无限
        :param gap: 每接收到多少个数据包返回一次数据
        :return: 用于在接收到监听目标时触发动作的可迭代对象
        """
        ...

    def stop(self) -> None:
        """停止监听，清空已监听到的列表"""
        ...

    def pause(self, clear: bool = True) -> None:
        """暂停监听
        :param clear: 是否清空已获取队列
        :return: None
        """
        ...

    def resume(self) -> None:
        """继续暂停的监听"""
        ...

    def clear(self) -> None:
        """清空监听到但还没返回的结果"""
        ...

    def wait_silent(self,
                    timeout: float = None,
                    targets_only: bool = False,
                    limit: int = 0) -> bool:
        """等待所有请求结束
        :param timeout: 超时时间（秒），为None时无限等待
        :param targets_only: 是否只等待targets指定的请求结束
        :param limit: 剩下多少个连接时视为结束
        :return: 返回是否等待成功
        """
        ...

    def _to_target(self, target_id: str, address: str, owner: ChromiumBase) -> None:
        """切换监听的页面对象
        :param target_id: 新页面对象_target_id
        :param address: 新页面对象address
        :param owner: 新页面对象
        :return: None
        """
        ...

    def _set_callback(self) -> None: ...

    def _requestWillBeSent(self, **kwargs) -> None: ...

    def _requestWillBeSentExtraInfo(self, **kwargs) -> None: ...

    def _response_received(self, **kwargs) -> None: ...

    def _responseReceivedExtraInfo(self, **kwargs) -> None: ...

    def _loading_finished(self, **kwargs) -> None: ...

    def _loading_failed(self, **kwargs) -> None: ...


class FrameListener(Listener):
    _owner: ChromiumFrame = ...
    _is_diff: bool = ...

    def __init__(self, owner: ChromiumFrame):
        """
        :param owner: ChromiumFrame对象
        """
        ...


class DataPacket(object):
    """数据包类"""

    tab_id: str = ...
    target: str = ...
    is_failed: bool = ...
    _raw_request: Optional[dict] = ...
    _raw_response: Optional[dict] = ...
    _raw_post_data: Optional[str] = ...
    _raw_body: Optional[str] = ...
    _raw_fail_info: Optional[dict] = ...
    _base64_body: bool = ...
    _request: Optional[Request] = ...
    _response: Optional[Response] = ...
    _fail_info: Optional[FailInfo] = ...
    _resource_type: Optional[str] = ...
    _requestExtraInfo: Optional[dict] = ...
    _responseExtraInfo: Optional[dict] = ...

    def __init__(self, tab_id: str, target: [str, bool]):
        """
        :param tab_id: 产生这个数据包的tab的id
        :param target: 监听目标
        """
        ...

    @property
    def url(self) -> str:
        """请求网址"""
        ...

    @property
    def method(self) -> str:
        """请求类型"""
        ...

    @property
    def frameId(self) -> str:
        """发出请求的frame id"""
        ...

    @property
    def resourceType(self) -> str:
        """资源类型"""
        ...

    @property
    def request(self) -> Request:
        """数据"""
        ...

    @property
    def response(self) -> Response:
        """Response数据"""
        ...

    @property
    def fail_info(self) -> Optional[FailInfo]:
        """请求失败数据"""
        ...

    def wait_extra_info(self, timeout: float = None) -> bool:
        """等待额外的信息加载完成
        :param timeout: 超时时间（秒），None为无限等待
        :return: 是否等待成功
        """
        ...

    @property
    def _request_extra_info(self) -> Optional[dict]: ...

    @property
    def _response_extra_info(self) -> Optional[dict]: ...


class Request(object):
    _data_packet: DataPacket = ...
    _request: dict = ...
    _raw_post_data: str = ...
    _postData: Optional[str] = ...

    url: str = ...
    _headers: Union[CaseInsensitiveDict, None] = ...
    method: str = ...

    urlFragment: str = ...
    hasPostData: bool = ...
    postDataEntries: List[dict] = ...
    mixedContentType: Literal['blockable', 'optionally-blockable', 'none'] = ...
    initialPriority: Literal['VeryLow', 'Low', 'Medium', 'High', 'VeryHigh'] = ...
    referrerPolicy: Literal['unsafe-url', 'no-referrer-when-downgrade', 'no-referrer', 'origin',
    'origin-when-cross-origin', 'same-origin', 'strict-origin', 'strict-origin-when-cross-origin'] = ...
    isLinkPreload: bool = ...
    trustTokenParams: dict = ...
    isSameSite: bool = ...

    def __init__(self,
                 data_packet: DataPacket,
                 raw_request: dict,
                 post_data: str):
        """
        :param data_packet: DataPacket对象
        :param raw_request: 未处理的请求数据
        :param post_data: post发送的数据
        """
        ...

    @property
    def headers(self) -> dict:
        """以大小写不敏感字典返回headers数据"""
        ...

    @property
    def params(self) -> dict:
        """dict格式返回请求url中的参数"""
        ...

    @property
    def postData(self) -> Any:
        """返回postData数据"""
        ...

    @property
    def cookies(self) -> List[dict]:
        """以list形式返回发送的cookies"""
        ...

    @property
    def extra_info(self) -> Optional[RequestExtraInfo]:
        """返回额外数据"""
        ...


class Response(object):
    _data_packet: DataPacket = ...
    _response: dict = ...
    _raw_body: str = ...
    _is_base64_body: bool = ...
    _body: Union[str, dict, bytes, None] = ...
    _headers: Union[dict, CaseInsensitiveDict, None] = ...

    url: str = ...
    status: int = ...
    statusText: str = ...
    headersText: str = ...
    mimeType: str = ...
    requestHeaders: dict = ...
    requestHeadersText: str = ...
    connectionReused: bool = ...
    connectionId = ...
    remoteIPAddress: str = ...
    remotePort: int = ...
    fromDiskCache: bool = ...
    fromServiceWorker: bool = ...
    fromPrefetchCache: bool = ...
    fromEarlyHints: bool = ...
    serviceWorkerRouterInfo: dict = ...
    encodedDataLength: int = ...
    timing: dict = ...
    serviceWorkerResponseSource: Literal['cache-storage', 'http-cache', 'fallback-code', 'network'] = ...
    responseTime: float = ...
    cacheStorageCacheName: str = ...
    protocol: str = ...
    alternateProtocolUsage: Literal['alternativeJobWonWithoutRace', 'alternativeJobWonRace', 'mainJobWonRace',
    'mappingMissing', 'broken', 'dnsAlpnH3JobWonWithoutRace', 'dnsAlpnH3JobWonRace', 'unspecifiedReason'] = ...
    securityState: Literal['unknown', 'neutral', 'insecure', 'secure', 'info', 'insecure-broken'] = ...
    securityDetails: dict = ...

    def __init__(self,
                 data_packet: DataPacket,
                 raw_response: dict,
                 raw_body: str,
                 base64_body: bool):
        """
        :param data_packet: DataPacket对象
        :param raw_response: 未处理的response信息
        :param raw_body: 未处理的body
        :param base64_body: body是否base64格式
        """
        ...

    @property
    def headers(self) -> CaseInsensitiveDict:
        """以大小写不敏感字典返回headers数据"""
        ...

    @property
    def raw_body(self) -> str:
        """返回未被处理的body文本"""
        ...

    @property
    def body(self) -> Any:
        """返回body内容，如果是json格式，自动进行转换，如果时图片格式，进行base64转换，其它格式直接返回文本"""
        ...

    @property
    def extra_info(self) -> Optional[ResponseExtraInfo]:
        """额外信息"""
        ...


class ExtraInfo(object):
    _extra_info: dict = ...

    def __init__(self, extra_info: dict):
        """
        :param extra_info: dict格式信息
        """
        ...

    @property
    def all_info(self) -> dict:
        """以dict形式返回所有额外信息"""
        ...


class RequestExtraInfo(ExtraInfo):
    requestId: str = ...
    associatedCookies: List[dict] = ...
    headers: dict = ...
    connectTiming: dict = ...
    clientSecurityState: dict = ...
    siteHasCookieInOtherPartition: bool = ...


class ResponseExtraInfo(ExtraInfo):
    requestId: str = ...
    blockedCookies: List[dict] = ...
    headers: dict = ...
    resourceIPAddressSpace: str = ...
    statusCode: int = ...
    headersText: str = ...
    cookiePartitionKey: str = ...
    cookiePartitionKeyOpaque: bool = ...


class FailInfo(object):
    _data_packet: DataPacket
    _fail_info: dict
    errorText: str
    canceled: bool
    blockedReason: Optional[str]
    corsErrorStatus: Optional[str]

    def __init__(self, data_packet: DataPacket, fail_info: dict):
        """
        :param data_packet: DataPacket对象
        :param fail_info: 返回的失败数据
        """
        ...