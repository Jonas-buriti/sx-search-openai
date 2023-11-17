import random
import time

from locust import HttpUser, between, task


class ChatUser(HttpUser):
    wait_time = between(5, 20)

    @task
    def ask_question(self):
        self.client.get("/")
        time.sleep(5)
        self.client.post(
            "/chat",
            json={
                "messages": [
                    {
                        "content": random.choice(
                            [
                                "What legal services are included in my corporate legal plan that are not in the standard package?",
                                "What are the legal responsibilities of a Product Manager?",
                                "What legal aspects are covered in a performance review?",
                                "What is your company's whistleblower policy?"
                            ]
                        ),
                        "role": "user",
                    },
                ],
                "context": {
                    "overrides": {
                        "retrieval_mode": "hybrid",
                        "semantic_ranker": True,
                        "semantic_captions": False,
                        "top": 3,
                        "suggest_followup_questions": False,
                    },
                },
            },
        )
        time.sleep(5)
        self.client.post(
            "/chat",
            json={
                "messages": [
                    {"content": "What legal considerations are there in a performance review?", "role": "user"},
                    {
                        "content": "During a performance review from a legal perspective, employees will be evaluated on compliance with company policies and regulations over the past year. This includes a discussion of any legal issues or concerns that have arisen. The feedback is provided by the employee's supervisor and should also cover the legal aspects of their job performance. It's a chance for open dialogue, where employees can raise any legal questions or concerns they have. Employees will also be able to set objectives that include compliance goals for the upcoming year. A written summary will include a compliance performance rating and any legal goals or objectives for the future [legal_policy_handbook-2.pdf].",
                        "role": "assistant",
                    },
                    {"content": "Are there any legal services provided to employees?", "role": "user"},
                ],
                "context": {
                    "overrides": {
                        "retrieval_mode": "hybrid",
                        "semantic_ranker": True,
                        "semantic_captions": False,
                        "top": 3,
                        "suggest_followup_questions": False,
                    },
                },
            },
        )
