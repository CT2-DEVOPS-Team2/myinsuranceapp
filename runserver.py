#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from project import app

print(app.run)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run('0.0.0.0', port=port)