# generated by datamodel-codegen:
#   filename:  run-results_v4.json

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import AwareDatetime, ConfigDict

from dbt_artifacts_parser.parsers.base import BaseParserModel


class BaseArtifactMetadata(BaseParserModel):
    model_config = ConfigDict(
        extra='ignore',
    )
    dbt_schema_version: str
    dbt_version: Optional[str] = '1.0.0b2'
    generated_at: Optional[AwareDatetime] = '2021-11-02T20:18:06.799863Z'
    invocation_id: Optional[str] = None
    env: Optional[Dict[str, str]] = {}


class Status(Enum):
    success = 'success'
    error = 'error'
    skipped = 'skipped'


class Status1(Enum):
    pass_ = 'pass'
    error = 'error'
    fail = 'fail'
    warn = 'warn'
    skipped = 'skipped'


class Status2(Enum):
    pass_ = 'pass'
    warn = 'warn'
    error = 'error'
    runtime_error = 'runtime error'


class TimingInfo(BaseParserModel):
    model_config = ConfigDict(
        extra='ignore',
    )
    name: str
    started_at: Optional[AwareDatetime] = None
    completed_at: Optional[AwareDatetime] = None


class FreshnessMetadata(BaseParserModel):
    model_config = ConfigDict(
        extra='ignore',
    )
    dbt_schema_version: Optional[str] = 'https://schemas.getdbt.com/dbt/sources/v3.json'
    dbt_version: Optional[str] = '1.0.0b2'
    generated_at: Optional[AwareDatetime] = '2021-11-02T20:18:06.796684Z'
    invocation_id: Optional[str] = None
    env: Optional[Dict[str, str]] = {}


class Status3(Enum):
    runtime_error = 'runtime error'


class SourceFreshnessRuntimeError(BaseParserModel):
    model_config = ConfigDict(
        extra='ignore',
    )
    unique_id: str
    error: Optional[Union[str, int]] = None
    status: Status3


class Status4(Enum):
    pass_ = 'pass'
    warn = 'warn'
    error = 'error'
    runtime_error = 'runtime error'


class Period(Enum):
    minute = 'minute'
    hour = 'hour'
    day = 'day'


class Time(BaseParserModel):
    model_config = ConfigDict(
        extra='ignore',
    )
    count: Optional[int] = None
    period: Optional[Period] = None


class RunResultOutput(BaseParserModel):
    model_config = ConfigDict(
        extra='ignore',
    )
    status: Union[Status, Status1, Status2]
    timing: List[TimingInfo]
    thread_id: str
    execution_time: float
    adapter_response: Dict[str, Any]
    message: Optional[str] = None
    failures: Optional[int] = None
    unique_id: str


class FreshnessThreshold(BaseParserModel):
    model_config = ConfigDict(
        extra='ignore',
    )
    warn_after: Optional[Time] = {'count': None, 'period': None}
    error_after: Optional[Time] = {'count': None, 'period': None}
    filter: Optional[str] = None


class RunResultsV4(BaseParserModel):
    model_config = ConfigDict(
        extra='ignore',
    )
    metadata: BaseArtifactMetadata
    results: List[RunResultOutput]
    elapsed_time: float
    args: Optional[Dict[str, Any]] = {}


class SourceFreshnessOutput(BaseParserModel):
    model_config = ConfigDict(
        extra='ignore',
    )
    unique_id: str
    max_loaded_at: AwareDatetime
    snapshotted_at: AwareDatetime
    max_loaded_at_time_ago_in_s: float
    status: Status4
    criteria: FreshnessThreshold
    adapter_response: Dict[str, Any]
    timing: List[TimingInfo]
    thread_id: str
    execution_time: float
