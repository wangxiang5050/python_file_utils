import fitz
import os


def convert_pdf_to_png(pdf_path):
    doc = fitz.open(pdf_path)  # open document

    for i, page in enumerate(doc):
        pix = page.get_pixmap()  # render page to an image
        if i > 0:
            pix.save(f"{get_file_prefix(pdf_path)}_{i}.png")
        else:
            pix.save(f"{get_file_prefix(pdf_path)}.png")


def get_file_prefix(file_path):
    basename_without_ext = os.path.splitext(os.path.basename(file_path))[0]
    dirname = os.path.dirname(os.path.abspath(file_path))
    return f"{dirname}/{basename_without_ext}"


if __name__ == "__main__":
    convert_pdf_to_png("resources/PMI_Certfication.pdf")
