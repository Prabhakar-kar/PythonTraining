# Define variables
agent_name = "Bond"  # Change this to any name
secret_message = "Meet me at the park"  # Change this to any message

# Encode the message
coded_message = secret_message.upper().replace(" ", "#") + "007" + agent_name

# Bonus: Add the length of the original message
coded_message_with_length = str(len(secret_message)) + "#" + coded_message

# Print results
print("Original message:", secret_message)
print("Coded message:", coded_message)
print("Coded message with bonus:", coded_message_with_length)
