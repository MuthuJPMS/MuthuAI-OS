from datetime import datetime

from core.infrastructure.config import config
from core.infrastructure.logger import logger
from core.infrastructure.dependency_container import container
from core.infrastructure.health_monitor import health_monitor

from core.events.event_bus import event_bus
from core.tools.tool_registry import tool_registry
from core.knowledge.knowledge_graph import knowledge_graph
from core.memory.v2.memory_bridge import memory_bridge


class StartupManager:


    def __init__(self):

        self.started = False



    def register_services(self):

        container.register("config", config)

        container.register("logger", logger)

        container.register("health_monitor", health_monitor)

        container.register("event_bus", event_bus)

        container.register("tool_registry", tool_registry)

        container.register("knowledge_graph", knowledge_graph)

        container.register("memory_bridge", memory_bridge)



    def register_health_components(self):

        components = [

            "Kernel",

            "Brain",

            "Mission",

            "Workflow",

            "Memory",

            "Knowledge Graph",

            "Tool Registry",

            "Event Bus",

            "Learning",

            "Security"

        ]


        for component in components:

            health_monitor.register_component(component)



    def start(self):

        if self.started:

            logger.warning("MuthuAI OS already started.")

            return


        logger.info("Starting MuthuAI OS...")


        config.initialize()

        self.register_services()

        self.register_health_components()


        self.started = True


        logger.info("MuthuAI OS startup completed.")


        return {

            "status": "started",

            "project": config.PROJECT_NAME,

            "version": config.VERSION,

            "environment": config.ENVIRONMENT,

            "services": container.list_services(),

            "health": health_monitor.overall_health(),

            "started_at": datetime.now().isoformat()

        }


startup_manager = StartupManager()