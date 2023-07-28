"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import orderoutput as shared_orderoutput
from ..shared import orderupdate as shared_orderupdate
from typing import Optional



@dataclasses.dataclass
class UpdateOrderRequest:
    order_id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'order_id', 'style': 'simple', 'explode': False }})
    order_update: shared_orderupdate.OrderUpdate = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    




@dataclasses.dataclass
class UpdateOrderResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    order_output: Optional[shared_orderoutput.OrderOutput] = dataclasses.field(default=None)
    r"""Successful Response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    
