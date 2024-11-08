import numpy as np
import cv2
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import List, Tuple, Optional
import logging
from pathlib import Path

# Logging konfigürasyonu
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class BoundingBox:
    """Bounding box verilerini tutan veri sınıfı"""
    x_min: float
    y_min: float
    x_max: float
    y_max: float
    class_id: int = 0

    @property
    def center(self) -> Tuple[float, float]:
        """Bounding box'ın merkez koordinatlarını döndürür"""
        return ((self.x_min + self.x_max) / 2, (self.y_min + self.y_max) / 2)
    
    @property
    def dimensions(self) -> Tuple[float, float]:
        """Bounding box'ın genişlik ve yüksekliğini döndürür"""
        return (self.x_max - self.x_min, self.y_max - self.y_min)

class YOLOFormatter:
    """YOLO format işlemleri için utility sınıfı"""
    
    @staticmethod
    def to_yolo_format(bbox: BoundingBox, img_width: int, img_height: int) -> str:
        """Bounding box'ı YOLO formatına dönüştürür"""
        x_center, y_center = bbox.center
        width, height = bbox.dimensions
        
        # Normalize coordinates
        x_center_norm = x_center / img_width
        y_center_norm = y_center / img_height
        width_norm = width / img_width
        height_norm = height / img_height
        
        return f"{bbox.class_id} {x_center_norm} {y_center_norm} {width_norm} {height_norm}"

class PolygonProcessor:
    """Polygon işlemleri için ana sınıf"""
    
    def __init__(self, image_path: str, label_path: str):
        """
        Args:
            image_path (str): Görüntü dosyasının yolu
            label_path (str): Label dosyasının yolu
        """
        self.image_path = Path(image_path)
        self.label_path = Path(label_path)
        self.image = None
        self.bbox = None
        
    def load_data(self) -> None:
        """Görüntü ve label verilerini yükler"""
        try:
            self.image = cv2.imread(str(self.image_path))
            if self.image is None:
                raise ValueError(f"Image could not be loaded from {self.image_path}")
            
            # Label dosyasını oku
            with open(self.label_path, 'r') as file:
                for line in file:
                    class_num = int(line.strip().split()[0])
                    coords = [float(value) for value in line.strip().split()[1:]]
                    self._process_coordinates(coords, class_num)
                    break
                    
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
    
    def _process_coordinates(self, coords: List[float], class_id: int) -> None:
        """Koordinatları işler ve bounding box oluşturur"""
        x_coords = np.array(coords[::2])
        y_coords = np.array(coords[1::2])
        
        self.bbox = BoundingBox(
            x_min=min(x_coords),
            y_min=min(y_coords),
            x_max=max(x_coords),
            y_max=max(y_coords),
            class_id=class_id
        )
    
    def save_yolo_format(self, output_path: str) -> None:
        """YOLO formatında koordinatları kaydeder"""
        if self.bbox is None or self.image is None:
            raise ValueError("Data must be loaded first")
            
        height, width = self.image.shape[:2]
        yolo_line = YOLOFormatter.to_yolo_format(self.bbox, width, height)
        
        try:
            with open(output_path, "w") as f:
                f.write(yolo_line + "\n")
            logger.info(f"YOLO format saved to {output_path}")
        except Exception as e:
            logger.error(f"Error saving YOLO format: {str(e)}")
            raise
    
    def draw_bbox(self) -> None:
        """Görüntü üzerine bounding box çizer"""
        if self.bbox is None or self.image is None:
            raise ValueError("Data must be loaded first")
            
        height, width = self.image.shape[:2]
        
        # Convert normalized coordinates to pixel coordinates
        x_min_px = int(self.bbox.x_min * width)
        y_min_px = int(self.bbox.y_min * height)
        x_max_px = int(self.bbox.x_max * width)
        y_max_px = int(self.bbox.y_max * height)
        
        cv2.rectangle(self.image, (x_min_px, y_min_px), (x_max_px, y_max_px), (0, 255, 0), 2)
    
    def display_image(self) -> None:
        """İşlenmiş görüntüyü gösterir"""
        if self.image is None:
            raise ValueError("Image must be loaded first")
            
        plt.figure(figsize=(10, 10))
        plt.imshow(cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB))
        plt.axis('off')
        plt.show()

def main():
    # Dosya yolları
    image_path = <image_path>
    label_path = <label_path>
    output_path = "output.txt"
    
    try:
        # İşlem pipeline'ı
        processor = PolygonProcessor(image_path, label_path)
        processor.load_data()
        processor.save_yolo_format(output_path)
        processor.draw_bbox()
        processor.display_image()
        
    except Exception as e:
        logger.error(f"An error occurred in main: {str(e)}")
        raise

if __name__ == "__main__":
    main()