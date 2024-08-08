# How to use

## Use directly
* model_file_path: Model file path(ONNX, TFLite)
* dataset_file_path: The path to the compressed file or the individual npy files where the delimiter of the input layer is used as the file name.

```bash
python3 src/inference.py --model_file_path tests/your_model_file.tflite --dataset_file_path tests/your_dataset_file.npy 
```

## Import and use

```python
inf_service = InferenceService(
        model_file_path="/your/model/file/path.onnx",
        dataset_file_path="/your/dataset/file/path.npy"
        )
inf_service.run() # Inference result file is in inf_service.result_file_path
```