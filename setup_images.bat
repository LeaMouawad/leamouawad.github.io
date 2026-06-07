@echo off
echo Copying project images to Portfolio folder...

set RENDU=D:\ALBA projects\10- Piscine d'un quartier\RENDU

copy "%RENDU%\untitled.19566.jpg"   "pool_render.jpg"
copy "%RENDU%\untitled.19ù65.jpg"   "pool_states.jpg"
copy "%RENDU%\move 1.jpg"           "pool_move_1.jpg"
copy "%RENDU%\move 2.jpg"           "pool_move_2.jpg"
copy "%RENDU%\move 3.jpg"           "pool_move_3.jpg"
copy "%RENDU%\move 4.jpg"           "pool_move_4.jpg"
copy "%RENDU%\move 5.jpg"           "pool_move_5.jpg"
copy "%RENDU%\move 6.jpg"           "pool_move_6.jpg"

echo Converting PDFs to images...
pdftoppm -r 150 -jpeg "%RENDU%\FINAL RENDU STRUCTURE- STORY BOARD.pdf" pool_roof_seq
pdftoppm -r 150 -jpeg "%RENDU%\FINAL RENDU STRUCTURE-D.pdf" pool_vent
pdftoppm -r 150 -jpeg "%RENDU%\FINAL RENDU STRUCTURE-DETAILS.pdf" pool_section

ren pool_roof_seq-1.jpg pool_roof_seq.jpg  2>nul
ren pool_vent-1.jpg pool_vent_full.jpg      2>nul
ren pool_section-1.jpg pool_section.jpg     2>nul

echo Done! Open index.html in your browser.
pause
