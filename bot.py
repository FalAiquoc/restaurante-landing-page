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
        print(f"[Agente Nexu] Processando mensagem: {message}")
        message = message.lower()
        
        if "cardápio" in message or "opções" in message:
            return self.get_dynamic_menu()
        elif "pedir" in message or "quero" in message:
            return self.handle_order_intent(message)
        else:
            return "Olá! Sou o assistente virtual do {}. Como posso ajudar com seu pedido hoje?".format(self.restaurant_name)

    def get_dynamic_menu(self):
        """
        Agente de Cardápio: Retorna apenas itens em estoque.
        """
        available_items = {k: v for k, v in self.menu.items() if v['stock'] > 0}
        response = "Nosso cardápio atualizado:
"
        for item, details in available_items.items():
            response += f"- {item.capitalize()}: R$ {details['price']}
"
        return response

    def handle_order_intent(self, message):
        """
        Agente de Vendas: Converte intenção em pedido real.
        """
        for item in self.menu:
            if item in message:
                if self.menu[item]['stock'] > 0:
                    self.menu[item]['stock'] -= 1
                    order = {"item": item, "status": "preparando", "time": time.time()}
                    self.active_orders.append(order)
                    return f"Perfeito! Seu pedido de {item} foi anotado e o Agente de Cozinha já foi notificado."
                else:
                    return f"Sinto muito, o item {item} acabou de esgotar. Gostaria de outra opção?"
        return "Não consegui identificar o item. Pode repetir o nome do prato?"

# Instanciação do sistema de agentes
if __name__ == "__main__":
    bot = NexuFoodAgent("Restaurante do Dyjann")
    
    # Simulação de interação
    print(bot.process_message("Quais são as opções do cardápio?"))
    print(bot.process_message("Eu quero pedir um almoço executivo"))
    print(f"Pedidos ativos no dashboard: {len(bot.active_orders)}")
