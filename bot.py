import json
import time

class NexuFoodAgent:
    """
    Agente inteligente para atendimento virtual e gestão de cardápio dinâmico.
    Utiliza lógica de processamento de linguagem natural (simulada) para
    converter intenções de clientes em pedidos no sistema.
    """

    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name
        self.menu = {
            "almoço executivo": {"price": 25.0, "stock": 10},
            "suco natural": {"price": 8.0, "stock": 50},
            "sobremesa": {"price": 12.0, "stock": 15}
        }
        self.active_orders = []

    def process_message(self, message):
        """
        Agente de Atendimento: Analisa a mensagem do cliente.
        """
        message = message.lower()
        if "cardápio" in message or "menu" in message:
            return self.get_formatted_menu()
        elif "pedir" in message or "quero" in message:
            return self.handle_order(message)
        return "Olá! Sou o assistente Nexu. Como posso ajudar seu restaurante hoje?"

    def get_formatted_menu(self):
        """
        Agente de Cardápio: Retorna o cardápio atualizado.
        """
        response = f"--- Cardápio {self.restaurant_name} ---
"
        for item, details in self.menu.items():
            stock_msg = "Disponível" if details["stock"] > 0 else "Esgotado"
            response += f"- {item.capitalize()}: R$ {details['price']:.2f} ({stock_msg})
"
        return response

    def handle_order(self, message):
        """
        Lógica de processamento de pedido simplificada.
        """
        for item in self.menu:
            if item in message:
                if self.menu[item]["stock"] > 0:
                    self.menu[item]["stock"] -= 1
                    order = {"item": item, "price": self.menu[item]["price"], "time": time.ctime()}
                    self.active_orders.append(order)
                    return f"Pedido confirmado: {item.capitalize()}! A IA de logística já está processando."
                return f"Desculpe, o item {item} está esgotado no momento."
        return "Não consegui identificar o item no seu pedido. Pode repetir?"

    def get_revenue(self):
        """
        Relatório financeiro agêntico.
        """
        total = sum(order["price"] for order in self.active_orders)
        return f"Faturamento Total via IA: R$ {total:.2f}"

# Simulação de uso
if __name__ == "__main__":
    bot = NexuFoodAgent("Restaurante do Dyjann")
    print(bot.process_message("Pode me mostrar o cardápio?"))
    print(bot.process_message("Quero pedir um almoço executivo"))
    print(bot.get_revenue())
