# Conditional Statements → Decide what to run based on conditions.

# -----------------------------------------------------------------------------------------------

# if elif else → Execute different code blocks based on conditions.
cpu_usage = 75  # This could come from a monitoring tool

if cpu_usage < 50:
    print("✅ CPU usage normal. No action needed.")
elif 50 <= cpu_usage < 80:
    print("⚠️ CPU usage high. Investigate running processes.")
else:
    print("🚨 CPU usage critical! Scale up or restart services.")

# -----------------------------------------------------------------------------------------------

'''
Control Statements → Change loop behavior.
break → Stop loop
continue → Skip to next iteration
'''

for i in range(5):
    if i == 3:
        break
    print(i)  # Stops when i = 3
for i in range(5):
    if i == 3:
        continue
    print(i)  # Skips printing when i = 3   

# -----------------------------------------------------------------------------------------------