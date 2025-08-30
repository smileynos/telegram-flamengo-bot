# main.py
chat_id=chat_id,
text="Escolha uma opção:",
reply_markup=KEYBOARD,
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
"""/start -> envia a mensagem de boas-vindas e as opções após 5s."""
chat_id = update.effective_chat.id
await context.bot.send_message(chat_id=chat_id, text=WELCOME_TEXT)
await asyncio.sleep(5)
await send_options(chat_id, context)


async def handle_any(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
"""Responde a QUALQUER mensagem recebida.


- Se a pessoa clicar em um dos botões, responde algo simples.
- Caso contrário, manda o texto fixo e, após 5s, as opções.
"""
chat_id = update.effective_chat.id
text = (update.message.text or "").strip() if update.message else ""


if text == OPTION_REGISTER:
await context.bot.send_message(
chat_id=chat_id,
text=(
"Perfeito! Para *Cadastrar venda de Ingressos*, envie os detalhes "
"(jogo, setor, quantidade, preço e forma de pagamento)."
),
parse_mode="Markdown",
)
return


if text == OPTION_REVIEW:
await context.bot.send_message(
chat_id=chat_id,
text=(
"Para *Avaliar Venda de ingresso*, mande o anúncio ou descrição que deseja avaliar."
),
parse_mode="Markdown",
)
return


# Qualquer outra mensagem -> comportamento padrão
await context.bot.send_message(chat_id=chat_id, text=WELCOME_TEXT)
await asyncio.sleep(5)
await send_options(chat_id, context)




def main() -> None:
token = os.environ.get("TELEGRAM_BOT_TOKEN")
if not token:
raise RuntimeError(
"Defina a variável de ambiente TELEGRAM_BOT_TOKEN com o token do BotFather."
)


app = Application.builder().token(token).build()


# /start
app.add_handler(CommandHandler("start", start))


# Qualquer mensagem (texto, áudio, foto, etc.)
app.add_handler(MessageHandler(filters.ALL, handle_any))


# Long polling (simples e não precisa de servidor público)
app.run_polling()




if __name__ == "__main__":
main()
