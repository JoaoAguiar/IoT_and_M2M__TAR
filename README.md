
# IoT & M2M

Our objective with this was to implement a rudimentary system that measured the ambient temperature and turned on a specific led according to the value measured. It also plays a sound accordingly to the range of values of temperature through.

The whole process was planned to be automatized and to follow a publish/subscribe pattern, meaning that the components would be connected to the RaspberryPi, which itself was to act as a publisher and given the temperature values, pursued an action with the components that are subscribed to the activity of the temperature sensor such as our personal computers, the LEDs and the speakers.

In this case, the digital sensor has to measure the temperature, registers it by sending it to the RaspberryPi, and it’s acting as a server sends it to our personal computer showcasing the actual ambient temperature and with that, turn a specific coloured LED and play a sound.

IMAGEM

## IoT Model

We can define an IoT system with a set of sensors, micro-controllers, and actuators. The sensors act as input to produce and collect data, and the microcontrollers process the data. Lastly, the actuators also function as output generating conditioned actions by a previously established set of instructions.

It is fundamental to create connections in the network capable of communicating M2M, where in the posterity, these data will be saved and processed so that they can control the components according to implemented rules. The IoT evolution implies the creation of protocols for data transmission in the network in IoT and M2M systems. Implementing a Publish-Subscribe communication model in IoT represents efficiency in the sense that much information is generated and effectively distributed to the interested parties.

A Publish-Subscribe model is composed by a set of messages, a topic that is associated with those messages, a subscription that refers to an interest in a particular topic and a subscriber that receives messages related to the topic that is subscribed to.

## MQTT

MQTT is an OASIS Advanced Message Queuing Protocol (AMQP) for the Internet of Things (IoT). It is a lightweight and efficient publish-subscribe network protocol that transports messages between devices over a TCP/IP connection. Besides that, it's bi-directional in terms of connections, which allows for messaging between the device to the cloud and the cloud to the device.

IMAGEM

We can identify three main components: Publish (MQTT client), Broker (MQTT server) and Subscriber (MQTT client).

The MQTT Client is a device that uses the protocol. It is responsible for establishing connection, create and publish messages or subscribe a topic.

An MQTT Server is responsible for accepting connections, publish messages and process requests. The server acts as an intermediary party that establishes rules between the publisher and the subscriber.


## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

