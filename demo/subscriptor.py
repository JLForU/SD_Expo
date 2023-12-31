
# IMPORTS
import paho.mqtt.client as mqtt



# MAIN FUNCTION DECLARATION
def main ( ) :

    print ("\n\n\n\n")


    # Establecer conexión.
    client = mqtt.Client()
    client.connect("localhost", 1883)

    # Recibir mensaje, especificando un tópico.
    client.subscribe("mytopic")
    client.on_message = on_message

    # Esperar más mensajes.
    try :
        client.loop_forever()
    except KeyboardInterrupt :
        # Handle the KeyboardInterrupt gracefully.
        pass

    # Establecer desconexión.
    client.disconnect()


    print ("\n\n\n\n")


# OTHER FUNCTIONS
def on_message(client, userdata, message):
    print(f"Received message '{message.payload.decode()}' on topic '{message.topic}'. UD: {userdata}")



# MAIN FUNCTION IMPLEMENTATION
if __name__ == "__main__" :
    main()




# To rest -->       
