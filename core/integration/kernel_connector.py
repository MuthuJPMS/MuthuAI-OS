from core.kernel.os_kernel import muthuai_kernel


class KernelConnector:


    def __init__(self):

        self.kernel = muthuai_kernel



    def submit_request(self, request):

        task = self.kernel.create_task(request)

        self.kernel.events.publish(
            "USER_REQUEST_RECEIVED",
            {
                "request": request
            }
        )

        return {
            "status": "accepted",
            "task": task
        }



    def system_status(self):

        return self.kernel.get_system_report()



    def request_approval(self, action):

        return self.kernel.request_permission(action)



kernel_connector = KernelConnector()