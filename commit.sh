#!/bin/bash
cd /home/pi/3D_Print_Server
git add .
git commit -m "Automated commit $(date)"
git push origin main
