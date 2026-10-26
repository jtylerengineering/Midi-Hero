# Midi-Hero

<img width="1259" height="748" alt="Screenshot 2026-10-25 at 8 49 10 PM" src="https://github.com/user-attachments/assets/2a44b629-d7a0-43fe-a944-70d07da6e545" />


## Description
The MIDI-Hero is a custom MIDI that mimics a *Guitar Hero* controller that was created as a Week 3 submission for Hack Club's ten week long Half Life event. The board is powered by a Waveshare ESP32 S3 microcontroller with <a href="https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/README.md">KMK</a> for firmware.

## Requirements
### Hardware
#### Component BOM
Below is a list of components you will need, and where I sourced them from.

| Component | Units (how many of each set you will have to buy) | Price per unit | Source | Shipping |
| --- | --- | --- | --- | --- |
| PCB | 1 | $8.80 | <a href="https://jlcpcb.com/">JLPCB</a> | 
| Keyboard Switch | 1 | 0.65 | <a href ="https://www.aliexpress.com/item/3256806385705423.html?spm=a2g0o.cart.0.0.618e38da4EeBiV&mp=1&pdp_npi=6%40dis%21USD%21USD%200.65%21USD%200.47%21%21USD%200.47%21%21%21%402101e80b17929768393442096e0ebc%2112000037704740809%21ct%21US%218282019388%21%211%210%21&_gl=1*jx3zfr*_gcl_aw*R0NMLjE3OTI1ODUxNzAuQ2p3S0NBanc1NnpXQmhCMEVpd0FkUE9RT2RLQnpWQTdQcnZsamVPZG4wN2ozaWRWVmZHLXhPNldWM1VNSnRFUW9aVGVzRElPT3pCbDhSb0MyS2dRQXZEX0J3RQ..*_gcl_dc*R0NMLjE3OTI1ODUxNzAuQ2p3S0NBanc1NnpXQmhCMEVpd0FkUE9RT2RLQnpWQTdQcnZsamVPZG4wN2ozaWRWVmZHLXhPNldWM1VNSnRFUW9aVGVzRElPT3pCbDhSb0MyS2dRQXZEX0J3RQ..*_gcl_au*NTU4NjE1ODIxLjE3OTI5NjU2NTA.*_ga*MjEzMzg5NTIwLjE3OTI5NzY2Mjk.*_ga_VED1YSGNC7*czE3OTI5NzY2MjkkbzEkZzEkdDE3OTI5NzY5NjUkajYwJGwwJGgw">Aliexpress</a> |
| Rotary Encoder | 1 | $2.30 |<a href ="[https://www.aliexpress.us/item/3256806414004024.html?spm=a2g0o.cart.0.0.618e38daTn9NyX&mp=1&pdp_npi=6%40dis%21USD%21USD+2.30%21USD+2.30%21%21USD+2.30%21%21%21%4021032e4e17929766291257345e0ef1%2112000037782871490%21ct%21US%218282019388%21%211%210%21&_gl=1*1kr33bv*_gcl_aw*R0NMLjE3OTI1ODUxNzAuQ2p3S0NBanc1NnpXQmhCMEVpd0FkUE9RT2RLQnpWQTdQcnZsamVPZG4wN2ozaWRWVmZHLXhPNldWM1VNSnRFUW9aVGVzRElPT3pCbDhSb0MyS2dRQXZEX0J3RQ..*_gcl_dc*R0NMLjE3OTI1ODUxNzAuQ2p3S0NBanc1NnpXQmhCMEVpd0FkUE9RT2RLQnpWQTdQcnZsamVPZG4wN2ozaWRWVmZHLXhPNldWM1VNSnRFUW9aVGVzRElPT3pCbDhSb0MyS2dRQXZEX0J3RQ..*_gcl_au*NTU4NjE1ODIxLjE3OTI5NjU2NTA.*_ga*MjEzMzg5NTIwLjE3OTI5NzY2Mjk.*_ga_VED1YSGNC7*czE3OTI5NzY2MjkkbzEkZzAkdDE3OTI5NzY2MjkkajYwJGwwJGgw&gatewayAdapt=glo2usa](https://www.aliexpress.us/item/3256813007942184.html?spm=a2g0o.cart.0.0.618e38da4EeBiV&mp=1&pdp_npi=6%40dis%21USD%21USD+2.29%21USD+2.29%21%21USD+2.29%21%21%21%402101e80b17929768630603039e0ebc%2112000060523754199%21ct%21US%218282019388%21%211%210%21&_gl=1*n93ae7*_gcl_aw*R0NMLjE3OTI1ODUxNzAuQ2p3S0NBanc1NnpXQmhCMEVpd0FkUE9RT2RLQnpWQTdQcnZsamVPZG4wN2ozaWRWVmZHLXhPNldWM1VNSnRFUW9aVGVzRElPT3pCbDhSb0MyS2dRQXZEX0J3RQ..*_gcl_dc*R0NMLjE3OTI1ODUxNzAuQ2p3S0NBanc1NnpXQmhCMEVpd0FkUE9RT2RLQnpWQTdQcnZsamVPZG4wN2ozaWRWVmZHLXhPNldWM1VNSnRFUW9aVGVzRElPT3pCbDhSb0MyS2dRQXZEX0J3RQ..*_gcl_au*NTU4NjE1ODIxLjE3OTI5NjU2NTA.*_ga*MjEzMzg5NTIwLjE3OTI5NzY2Mjk.*_ga_VED1YSGNC7*czE3OTI5NzY2MjkkbzEkZzEkdDE3OTI5NzY4MzkkajYwJGwwJGgw&gatewayAdapt=glo2usa)">Aliexpress</a> |
| PS2 Joystick | 1 | $3.02 | <a href="https://www.aliexpress.us/item/3256805763176642.html?spm=a2g0o.cart.0.0.618e38da4EeBiV&mp=1&pdp_npi=6%40dis%21USD%21USD+3.02%21USD+3.02%21%21USD+3.02%21%21%21%402101e80b17929768630603039e0ebc%2112000035000335220%21ct%21US%218282019388%21%211%210%21&_gl=1*7f4qeu*_gcl_aw*R0NMLjE3OTI1ODUxNzAuQ2p3S0NBanc1NnpXQmhCMEVpd0FkUE9RT2RLQnpWQTdQcnZsamVPZG4wN2ozaWRWVmZHLXhPNldWM1VNSnRFUW9aVGVzRElPT3pCbDhSb0MyS2dRQXZEX0J3RQ..*_gcl_dc*R0NMLjE3OTI1ODUxNzAuQ2p3S0NBanc1NnpXQmhCMEVpd0FkUE9RT2RLQnpWQTdQcnZsamVPZG4wN2ozaWRWVmZHLXhPNldWM1VNSnRFUW9aVGVzRElPT3pCbDhSb0MyS2dRQXZEX0J3RQ..*_gcl_au*NTU4NjE1ODIxLjE3OTI5NjU2NTA.*_ga*MjEzMzg5NTIwLjE3OTI5NzY2Mjk.*_ga_VED1YSGNC7*czE3OTI5NzY2MjkkbzEkZzEkdDE3OTI5NzY4NzMkajI2JGwwJGgw&gatewayAdapt=glo2usa">Aliexpress</a> |
| tax/shipping | $8.70 | --- | --- | --- |
| total | $30.08 |

#### Other
Other than the above, you will need:
1. The PCB. I used JLPCB for manufacturing, but whatever service fits your fancy will do.
2. Soldering supplies (iron, solder, etc.)
3. A computer to work with the firmware
4. a 3d printer for keycaps, case, etc.

### Firmware

## Assembly
>[!note]
>A full set of assembly instructions will be released during week 8, once I have photos.

### Electrical Parts
<img width="1259" height="748" alt="Screenshot 2026-10-25 at 8 50 48 PM" src="https://github.com/user-attachments/assets/5977b5a5-7759-4057-854f-37c2c3d7f9df" />

This is the number of each component from the 'Requirements' section you will need for one assembly per the current version.

| Component | Quantity |
| --- | --- |
| PCB | 1 |
| Keyboard Switch | 5 |
| Waveshare ESP32-S3 | 1 |
| PS2 Joystick | 1 |
| Rotary encoder | 1 |

### 3D printing
If you want the case and keycaps, you will need to either print them yourself or get them printed. I used PLA for my filament. Something to keep in mind, however, is that you will need a 0.2 mm nozzle for your printer. the tolerance needs to be rather tight, and you won't get that very well with a 0.4 mm nozzle.
All of the STL files are in the STL folder.

## Quick Links
**Most links are closed until week 8, to ensure that the final product is functioning as well as possible**
[Onshape Link-- closed]()

[MakerWorld Project-- closed]()

