from datetime import datetime


class MuthuAIException(Exception):

    def __init__(self, message, code="MUTHUAI_ERROR"):

        super().__init__(message)

        self.message = message

        self.code = code

        self.timestamp = datetime.now().isoformat()

    def to_dict(self):

        return {

            "status": "error",

            "error_code": self.code,

            "message": self.message,

            "timestamp": self.timestamp

        }


class ConfigurationError(MuthuAIException):

    def __init__(self, message):

        super().__init__(

            message,

            "CONFIGURATION_ERROR"

        )


class PermissionDeniedError(MuthuAIException):

    def __init__(self, message):

        super().__init__(

            message,

            "PERMISSION_DENIED"

        )


class AgentExecutionError(MuthuAIException):

    def __init__(self, message):

        super().__init__(

            message,

            "AGENT_EXECUTION_ERROR"

        )


class ToolExecutionError(MuthuAIException):

    def __init__(self, message):

        super().__init__(

            message,

            "TOOL_EXECUTION_ERROR"

        )


class WorkflowError(MuthuAIException):

    def __init__(self, message):

        super().__init__(

            message,

            "WORKFLOW_ERROR"

        )


class MemoryError(MuthuAIException):

    def __init__(self, message):

        super().__init__(

            message,

            "MEMORY_ERROR"

        )


class KnowledgeGraphError(MuthuAIException):

    def __init__(self, message):

        super().__init__(

            message,

            "KNOWLEDGE_GRAPH_ERROR"

        )


class ValidationError(MuthuAIException):

    def __init__(self, message):

        super().__init__(

            message,

            "VALIDATION_ERROR"

        )