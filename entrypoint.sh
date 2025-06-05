#!/bin/bash

# Start Odoo service in the background
/usr/bin/odoo &
ODOO_PID=$!

# Wait for Odoo to be ready (you might want to implement a better check here)
sleep 10

# Upgrade addons
/usr/bin/odoo -d IMM -u material_registry

# Wait for Odoo process to finish
wait $ODOO_PID