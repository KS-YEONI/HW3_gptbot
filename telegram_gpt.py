from openai import OpenAI
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

#chatgpt function
def chat_gpt(prompt):
    client = OpenAI(
        api_key = "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"
    )
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    result = completion.choices[0].message.content
    return result


#telegram
token = "6419179666:AAHBYnaxOF5_DvVYCsE0RauGx6ZHIfCbY2Y"

async def gpt(update, context):
    prompt = update.message.text
    gpt_result = chat_gpt(prompt)
    await update.message.reply_text(gpt_result)

def main():
    #bot token
    application = Application.builder().token(token).build()

    # 텔레그램 user 메시지 받아 gpt 입력으로 넣음.
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, gpt))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
