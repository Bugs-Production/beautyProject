from PIL import Image
import pillow_heif


def convert_heic_to_png(heic_filename, output_filename):
    try:
        heif_file = pillow_heif.read_heif(heic_filename)
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",
        )
        image.save(output_filename, format="PNG")
        return True  # Успешно сконвертировано
    except Exception as e:
        print(f"Ошибка при конвертации изображения: {str(e)}")
        return False  # Произошла ошибка при конвертации
