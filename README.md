# gimp-povray-crop

Gimp plugin, for [povray](http://www.povray.org/) generated image files. "Template Folder" is used for only alpha selection of the images. 
"Input Folder" is used for images that are to be cropped. Via "ray-tracing, [povray](http://www.povray.org/) generates the images. However, you may only be interested in the specific object in the scene.
Especially if you are game developer. 

__Idea is:__ 
* First generate the scene all with the other objects (of course with animation). 
* Second, generate the scene only with the desired object, giving the [povray](http://www.povray.org/) "+ua" parameter to make the background transparent.
* Then by using this plugin, you can select and cut your interested object from the scene (because of animation, there are many images to crop!).

__Example:__

| Input        | Template           | Out  |
| ------------- |-------------|-----|
| ![](./example/input/glass01.png)| ![](./example/template/glass01.png)|![](./example/out/glass01.png)||



# progressbar
* This library is copied from [progressbar](https://github.com/WoLpH/python-progressbar/tree/develop/progressbar).
* In this plugin I use another plugin, which also uses the progressbar on the UI. Therefore, I used [progressbar](https://github.com/WoLpH/python-progressbar/tree/develop/progressbar) this library. Not that, progress is written to the console. Therefore, you need to start gimp from console.

# Links
* [Use Python to write plug-ins for GIMP](https://www.ibm.com/developerworks/library/os-autogimp/index.html)
* [Gimp-Python](http://www.jamesh.id.au/software/pygimp/)
* [Batch image manipulation using Python and GIMP](https://ntcore.com/?p=509)
* [Close current file/view/display without saving it or beeing asked to do so](https://stackoverflow.com/questions/42026126/close-current-file-view-display-without-saving-it-or-beeing-asked-to-do-so)
* [Hacking:Plugins](https://wiki.gimp.org/wiki/Hacking:Plugins)