#!/usr/bin/env python

from gimpfu import *
import os
from progressbar import Bar, Percentage, ProgressBar


def povray_crop_all(x, y, width, height, input_folder, template_folder, output_folder):
    pdb.gimp_progress_init("Cropping ", None)
    files = os.listdir(input_folder)
    idx = 0
    progress_bar = ProgressBar(widgets=[Percentage(), Bar()], maxval=len(files)).start()
    for image_candidate_file in files:
        idx = idx + 1
        try:
            input_path = os.path.join(input_folder, image_candidate_file)
            template_path = os.path.join(template_folder, image_candidate_file)
            image = None

            if image_candidate_file.lower().endswith('.png'):
                image = pdb.file_png_load(input_path, input_path)
            else:
                continue

            template_layer = pdb.gimp_file_load_layer(image, template_path)
            pdb.gimp_image_set_active_layer(image, image.layers[0])
            pdb.gimp_image_insert_layer(image, template_layer, None, -1)

            if image is None:
                fail("ERROR: None Image")
                return
            if len(image.layers) != 2:
                fail("ERROR: layer count=" + str(len(image.layers)))

            crop(image, image.layers[1], image.layers[0], x, y, width, height, output_folder)

        except Exception as err:
            fail("Unexpected error: " + str(err))

        pdb.gimp_progress_set_text("Processed: " + str(float(idx) / len(files)))
        pdb.gimp_progress_update(float(idx) / len(files))
        progress_bar.update(idx)

    progress_bar.finish()
    pdb.gimp_progress_end()


def crop(img, layer_real, layer_template, x, y, width, height, output_folder):
    pdb.gimp_layer_add_alpha(layer_real)
    pdb.gimp_layer_set_opacity(layer_real, 100)  # 80
    layer_real.opacity = 100.0  # 90

    pdb.gimp_selection_layer_alpha(layer_template)
    pdb.gimp_selection_invert(img)
    pdb.gimp_edit_clear(layer_real)

    pdb.gimp_image_crop(img, width, height, x, y)
    #pdb.gimp_image_scale(img, 128, 128)

    pdb.gimp_image_remove_layer(img, layer_template)
    img.merge_visible_layers(NORMAL_MODE)
    image_full_name = pdb.gimp_image_get_filename(img)

    exp_name = os.path.basename(image_full_name)
    export_full_name = os.path.join(output_folder, exp_name)
    pdb.file_png_save(img, img.layers[0], export_full_name, exp_name, False, 9, False, False, False, False, False)


register(
    "povray_crop",
    "Crops povray generated images according to template.",
    "",
    "erdinc",
    "GPL",
    "2018",
    "Povray Crop",
    "",
    [
        # hint
        (PF_INT, "x", "x", 0),
        (PF_INT, "y", "y", 0),
        (PF_INT, "width", "w", 100),
        (PF_INT, "height", "h", 100),

        (PF_DIRNAME, "inputFolder", "Input Folder", ""),
        (PF_DIRNAME, "templateFolder", "Template Folder", ""),
        (PF_DIRNAME, "outputFolder", "Output Folder", "")
    ],
    [],
    povray_crop_all,
    menu="<Image>/File/"
    )

main()
