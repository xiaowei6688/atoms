# -*- coding: utf-8 -*-
"""
@File        : response.py
@Author      : Lu Wei
@Time        : 2022/12/29 4:02 下午
@Description :
"""
# -*- coding: utf-8 -*-
"""
@File        : response.py
@Author      : liuda
@Time        : 2022/8/5 14:03
@Description : response响应体
"""
from enum import Enum


class SourceTypeErr(str, Enum):
    """数据源类型 err"""

    UNKNOWN = "未知数据源"
    INVALID_CONFIG = "无效配置"


class SourceErr(str, Enum):
    """数据源 err"""

    DUPLICATE_NAME = "您输入的数据源名称已存在，请重新输入"
    INVALID_NAME = "数据源名称必须以字母、数字、下划线（_）组合，且不能以数字和下划线（_）开头。"
    INVALID_ADMINS = "无效数据库管理员"
    FORBIDDEN_DEL_SELF = "禁止删除本人"
    FAIL_CONNECT = "数据源连通性测试未通过，请检查设置信息！"
    NOT_FOUND = "数据源不存在"
    PERMISSION_DENIED = "无删除权限"
    RELATED_TASK = "存在关联的任务配置，请将关联项移除后，再进行删除操作！"


class AuthError(Enum):
    FAIL_AUTH = "请登录"
    NO_ORG = "请携带组织信息"
    FAKE_ORG = "请携带正确组织信息"
    FAIL_PHONE = "请使用正确的手机号"


class PhoneCodeResponse(Enum):
    OPERATORION_TOO_OFTEN = "操作太频繁，请等待"
    IMG_ERROR = "图形验证码错误"
    SEND_ERROR = "短信验证码发送失败，请稍后再试"
    PHONE_ERROR = "用户没有手机号，请先绑定"
    HAS_LOCKED = "该手机号已被锁定，暂时无法获取短信验证码"
    HAS_EXPIRED = "该短信验证码错误，需要重新获取"
    SUCCESS = "验证码已发送到你的手机，5分钟以内输入有效"


class LoginResponse(Enum):
    USERINFO_ERROR = "登录账号或密码错误"
    MULTIPLE_OBJECTS_RETURNED_ERROR = "账号查询异常，请联系管理员"
    TYPE_ERROR = "错误的登录方式"
    PHONE_UNREGISTERED_ERROR = "该手机号尚未注册"
    PHONE_MAX_RETRY_ERROR = "连续输错5次，该手机号已被锁定，过20分钟之后您再访问登录即可。"
    PHONE_RETRY_ERROR = "短信验证码输错{}次，连续输错5次，手机号将被锁定"


class RegisterResponse(Enum):
    SUCCESS = "注册成功"
    FAIL = "注册失败"


class ResetPWResponse(Enum):
    SUCCESS = "修改成功，请牢记新的登录密码"
    FAIL = "设置密码失败，请重新操作"


class EditResponse(Enum):
    CAN_NOT_EDIT = "无法编辑"


class DtProjectResponse(Enum):
    RULE_INVALID = "项目编号只能包含数字，字母或者下划线"
    LEN_INVALID = "项目编号长度要大于等于3位，小于等于25位"
    EXISTS = "项目编号已存在，请重新填写"
    NOT_FOUND = "项目不存在"
    NOT_FOUND_OR_FORBID = "项目不存在或您无权限"
    CONTROLS_NOT_NULL = "负责人不能为空"
    SELF_DONT_DELETE_CONTROLS = "项目创建人不能删除"
    SELF_NOT_IN_CONTROLS = "负责人需要包含您自己"
    HAS_TASK = "存在关联的任务配置，请将关联项移除后，再进行删除操作"


class PermissionResponse(Enum):
    NO_PERMISSION = "您没有权限"


class PaginationErr(str, Enum):
    """分页err"""

    INVALID = "分页参数无效"


class UserError(Enum):
    CONFIRM_PASSWORD_ERROR = "两次输入的密码不一致，请重新输入"
    FAILED_EXISTS = "{}已存在, 请重新填写"
    FAILED_USERNAME = "用户账号错误,  3-25字符，可以包含字母、数字、下划线"
    FAILED_NICK_NAME = "用户昵称错误, 3-25字符，可以包含汉字、字母、数字、下划线"
    FAILED_ROLE_NAME = "角色名错误, 3-25字符，可以包含汉字、字母、数字、下划线"
    FAILED_PASSWORD = "6位以上字符，包含英文大小写+数字组合"
    USER_EXISTS = "账号名已存在，请重新填写"


class OrgError(Enum):
    ORG_NAME_EXISTS = "组织名称已存在,请重新填写"
    FAILED_ORG_NAME = "组织名错误, 3-25字符，可以包含汉字、字母、数字、下划线"
    DESC_LENGTH_ERROR = "组织描述不得超过80个字符"
    ROLE_LENGTH_ERROR = "角色描述不得超过200个字符"


class RoleError(Enum):
    DELETE_ERROR = "删除失败，请联系系统管理员"
    DELETE_SUCCESS = "删除成功"
    ISVALID = "添加失败，请联系系统管理员"
    USER_NOT_DELETED = "角色已经关联用户，请将关联用户移除后，再进行删除操作！"
    HAVE_FLOW = "角色已经关联流程，请先取消关联后，再进行删除操作！"


class TaskErr(str, Enum):
    """任务 err"""

    DUPLICATE_NAME = "您输入的任务组名称已存在，请重新输入"
    INVALID_NAME = "任务组名称必须以字母、数字、下划线（_）组合，且不能以数字和下划线（_）开头。"
    INVALID_PARTICIANTS = "无效参与人"
    FORBIDDEN_DEL_SELF = "禁止删除本人"
    DESC_MAX_LENGTH = "任务描述不得超过{max_length}个字符"
    INVALID_FROM_SOURCE = "无效数据来源"
    NOT_FOUND_FROM_SOURCE = "数据来源不存在"
    FORBIDDEN_FROM_SOURCE = "无该数据来源的采集权限"
    INVALID_TO_SOURCE = "无效数据去向"
    NOT_FOUND_TO_SOURCE = "数据去向不存在"
    INVALID_START_AT = "无效开始时间"
    INVALID_END_AT = "无效结束时间"
    INVALID_TIMING = "无效起止时间"
    INVALID_CRONTAB = "无效crontab表达式"
    NOT_FOUND_FROM_TABLE = "来源表不存在"
    NOT_FOUND_TO_TABLE = "目标表不存在"
    DUPLICATE_FROM_TABLE = "来源表重复"
    DUPLICATE_TO_TABLE = "目标表重复"
    TO_TABLE_DESC_ISNULL = "目标表描述不能为空"
    TO_FIELD_DESC_ISNULL = "目标字段描述不能为空"
    MAX_SUB_TASKS = "单次任务最多支持{num}张表的批量设置"
    INVALID_TABLE_MAP = "无效表映射关系"
    EXPIRED_TABLE_AUTH = "表授权已过期"
    SYNC_FROM_FIELD_ISNULL = "目标表最新的字段信息"
    INVALID_FROM_FIELD = "无效来源字段"
    INVALID_TO_FIELD = "无效目标字段"
    TO_FIELD_NOT_NULL_MUST_SYNC = "目标表中目标字段不可为空时，必须指定来源字段同步"
    INVALID_FIELD_MAP = "无效字段对应关系"
    NOT_FOUND = "任务组不存在"
    SUB_REVIEWING_OR_ONLINE = "该任务组存在任务处于审批中或者上线状态，不支持删除操作"
    INVALID_PARAMS = "无效参数"
    INVALID_CYCLE = "无效任务周期"
    INVALIDA_DATETIME = "无效时间"
    NO_THROTTLE_LIMIT = "请输入限流速率"
    INVALID_AUTH_RANGE = "任务运行的起止时间设置应保证数据采集权限周期内"
    DRAFT_INVALID_AUTH_RANGE = "任务运行的起止时间设置应保证在所有表的数据采集权限周期内，可以选择小范围日期区间，再前往编辑特定子任务信息进行变更操作"
    NO_SYNC = "任务({from_table}->{to_table})至少选择一个字段进行同步"


class SyncTypeErr(str, Enum):
    """同步策略 err"""

    NOT_FOUND = "同步策略不存在"
    INVALID_INCR_CONFIG = "无效增量配置"


class TaskTypeErr(str, Enum):
    """作业类型 err"""

    NOT_FOUND = "作业类型不存在"


class HistorySyncTypeErr(str, Enum):
    """历史数据首次拉取方式 err"""

    NOT_FOUND = "历史数据首次拉取方式不存在"
    INVALID_START_AT = "无效首次拉取起始时间"
    NOT_FOUND_INCR_FIELD = "增量字段不存在"


class TaskTableErr(str, Enum):
    """子任务 err"""

    NOT_FOUND = "任务不存在"
    FORBIDDEN_DEL_STATUS = "该任务处于{status}，不支持删除操作"
    INVALID_STATUS = "无效状态"
    DUPLICATE = "任务重复"
    UNKNOWN = "未知任务"
    OPERATE_CONCURRENCY = "存在任务并发操作, 请稍后重试"
    INVALID_SUPPLYMENT_DATE = "无效补录日期"
    INVALID_SYNC_TYPE = "无效同步策略"

    ONLINE_OPERATION_INVALID_STATUS = "只允许对下线状态的任务进行上线操作！"
    OFFLINE_OPERATION_INVALID_STATUS = "只允许对上线状态的任务进行下线操作！"
    REDO_OPERATION_INVALID_STATUS = "只允许重跑普通实例为非运行态的任务！"
    STOP_OPERATION_INVALID_STATUS = "只允许终止存在正在运行态实例的任务！"
    SUPPLYMENT_OPERATION_INVALID_STATUS = "只允许对上线状态的任务进行补录操作！"


class CollectApplyExamineErr(Enum):
    STATUS_ERROR = "当前状态错误"
    INVALID_AGENDA_ID = "无效的待办id"
    EXAMINING = "正在处理, 请稍后再试"


class ConfigErr(str, Enum):
    """系统配置 err"""

    NOT_FOUND = "该配置项不存在"


class ColumnErr(str, Enum):
    """自定义展示列 err"""

    INVALID_TYPE = "无效类型"
    DUPLICATE = "存在重复列"
    DISABLE_COLUMNS = "不能修改默认列"
    UNKNOWN = "未知列"


class WarningRuleErr(str, Enum):
    INVALID = "无效配置"


class AppFlowErr(str, Enum):
    NOT_FOUND = "不存在"


class InstanceErr(str, Enum):
    NOT_FOUND = "不存在"
    DUPLICATE = "实例重复"
    UNKNOWN = "未知任务"
    INVALID_STATUS = "无效状态"
    OPERATE_CONCURRENCY = "存在并发操作, 请稍后重试"
    FORBIDDEN_BATCH_REDO = "禁止批量重跑"
    INVALIDATE_DATE = "无效日期"

    REDO_OPERATION_INVALID_STATUS = "只允许重跑正在非运行态的实例！"
    STOP_OPERATION_INVALID_STATUS = "只允许终止正在运行态的实例！"


class SupplymentInstanceErr(str, Enum):
    NOT_FOUND = "不存在"
    DUPLICATE = "实例重复"
    UNKNOWN = "未知任务"
    INVALID_STATUS = "无效状态"
    OPERATE_CONCURRENCY = "存在并发操作, 请稍后重试"
    FORBIDDEN_BATCH_REDO = "禁止批量重跑"
    INVALIDATE_DATE = "无效日期"

    REDO_OPERATION_INVALID_STATUS = "只允许重跑正在非运行态的实例！"
    STOP_OPERATION_INVALID_STATUS = "只允许终止正在运行态的实例！"


class StatisticsErr(str, Enum):
    QUERY_TIMEDELTA = "查询条件：时间范围超过90天"


class DtProjectMemberErr(str, Enum):
    DUPLICATE = "不可重复申请"
    NOT_FOUND = "申请不存在"
    HAVE_TASK = "用户已经关联同步任务，请将关联关系移除后，再进行成员移除操作！"


class CollectApplyTableErr(str, Enum):
    TARGET_NOT_FOUND = "目标表不存在"
