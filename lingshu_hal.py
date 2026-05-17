"""
文件名: lingshu_hal.py
项目: 灵枢操作系统 (Lingshu OS)
职责: 硬件抽象层 (HAL) 标准接口定义
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, Union

class LingshuHAL(ABC):
    """
    灵枢核心硬件抽象层基类。
    所有适配芯片（如华为昇腾、RISC-V K3）必须实现以下5个核心API。
    """

    @abstractmethod
    def load_model(self, model_path: str, target_device: str) -> bool:
        """
        1. 加载AI模型：将模型文件载入芯片内存或NPU。
        [设计依据: 灵枢细化路线 423条]
        """
        pass

    @abstractmethod
    def infer(self, input_data: Any) -> bool:
        """
        2. 触发推理：执行端侧计算任务。
        [设计依据: 实时性要求 <10ms, 见细化路线 430条]
        """
        pass

    @abstractmethod
    def get_result(self) -> Dict[str, Any]:
        """
        3. 获取结果：返回符合灵枢JSON协议的结构化数据。
        [设计依据: 十天开发总览 Day 3-4 协议定义]
        """
        pass

    @abstractmethod
    def set_power_mode(self, mode: str) -> bool:
        """
        4. 功耗管理：动态调整端侧芯片的运行模式。
        """
        pass

    @abstractmethod
    def report_status(self) -> Dict[str, Union[float, str]]:
        """
        5. 状态汇报：汇报算力占用、延迟、功耗等信息。
        [设计依据: 用于灵枢·枢的任务路由决策, 见细化路线 422条]
        """
        pass