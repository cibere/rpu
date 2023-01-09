from enum import Enum

__all__ = [
    "HTTPCodes",
    "SuccessHTTPCodes",
    "RedirectHTTPCodes",
    "InfoHTTPCodes",
    "ServerErrorHTTPCodes",
    "ClientErrorHTTPCodes",
]


class ClientErrorHTTPCodes(Enum):
    """A collection of client error http codes."""

    bad_request = 400
    unauthorized = 401
    payment_required = 402
    forbidden = 403
    not_found = 404
    method_not_allowed = 405
    not_acceptable = 406
    proxy_auth_required = 407
    request_timeout = 408
    conflict = 409
    gone = 410
    length_required = 411
    precondition_failed = 412
    payload_too_large = 413
    uri_too_long = 414
    unsupported_media_type = 415
    range_not_satisfiable = 416
    expectation_failed = 417
    im_a_teapot = 418
    unprocessable_entity = 422
    too_early = 425
    upgrade_required = 426
    precondition_required = 428
    too_many_requests = 429
    request_header_fields_too_large = 431
    unavailable_for_legal_reasons = 451


class ServerErrorHTTPCodes(Enum):
    """A collection of server error http codes"""

    internal_server_error = 500
    not_implemented = 501
    bad_gateway = 502
    service_unavailable = 503
    gateway_timeout = 504
    http_version_not_supported = 505
    variant_also_negotiates = 506
    insufficient_storage = 507
    loop_detected = 508
    not_extended = 510
    network_auth_required = 511


class InfoHTTPCodes(Enum):
    """A collection of info error http codes"""

    continue_ = 100
    switching_protocols = 101
    early_hints = 103


class SuccessHTTPCodes(Enum):
    """A collection of successful http codes"""

    ok = 200
    created = 201
    accepted = 202
    non_authoritive_info = 203
    no_context = 204
    reset_content = 205
    partial_content = 206


class RedirectHTTPCodes(Enum):
    """A collection of redirecting http codes"""

    multiple_choices = 300
    moved_permanently = 301
    found = 302
    see_other = 303
    not_modified = 304
    temp_redirect = 307
    perm_redirect = 308


class HTTPCodes:
    """A class which holds all of the collections of http codes"""

    successfull = SuccessHTTPCodes
    redirect = RedirectHTTPCodes
    info = InfoHTTPCodes
    server_error = ServerErrorHTTPCodes
    client_error = ClientErrorHTTPCodes
