# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount
from flask import Config

from botbuilder.ai.qna import QnAMaker, QnAMakerEndpoint
from datetime import datetime

def __init__(self, config: Config):
   self.qna_maker = QnAMaker(
      QnAMakerEndpoint(
         knowledge_base_id=config["QNA_KNOWLEDGEBASE_ID"],
         endpoint_key=config["QNA_ENDPOINT_KEY"],
         host=config["QNA_ENDPOINT_HOST"],
   )
)

class EchoBot(ActivityHandler):
    async def on_members_added_activity(
        self, members_added: [ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Oie pessoal!")

    async def on_message_activity(self, turn_context: TurnContext):
        return await turn_context.send_activity(
            MessageFactory.text(f"Você disse: {turn_context.activity.text}?")
        )
    
    async def on_turn(self, context: TurnContext):
        # Check to see if this activity is an incoming message.
        # (It could theoretically be another type of activity.)
        if context.activity.type == "message" and context.activity.text:
            # Check to see if the user sent a simple "quit" message.
            if context.activity.text.lower() == "horas":
                now = datetime.now()
                current_time = now.strftime("%H:%M")
                # Send a reply.
                await context.send_activity(current_time)
                # exit(0)
            elif context.activity.text.lower() == "oi":
                # Echo the message text back to the user.
                await context.send_activity(f"Oi {context.activity.recipient.name}, tudo bem?\
                    O que deseja saber?\n\
                        O que posso te dizer por enquanto são as horas e o dia da semana...\n\
                            Sou nova ainda :)")
            elif context.activity.text.lower() == "dia da semana":
                now = datetime.now()
                current_time = now.strftime("%A")
                # Send a reply.
                await context.send_activity(current_time)
            
            else:
                await context.send_activity("O que posso te dizer por enquanto são as horas e o dia da semana...\n\
                    Digite 'horas' ou 'dia da semana' e eu te respondo!!")