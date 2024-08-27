import argparse

from loguru import logger

from netspresso_inference_package.inference.inference_service import InferenceService


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_file_path', type=str)
    parser.add_argument('--dataset_file_path', type=str)
    return parser.parse_args()
    


def main(model_file_path:str, dataset_file_path:str):
    inf_service = InferenceService(
        model_file_path,
        )
    
    for k, v in inf_service.inputs.items():
        print(f"Input {k}: {v.dtype}")
        print(f"Input {k}: {v.format}")
        print(f"Input {k}: {v.height}")
        print(f"Input {k}: {v.width}")
        print(f"Input {k}: {v.key}")
        print(f"Input {k}: {v.location}")
        print(f"Input {k}: {v.name}")
        print(f"Input {k}: {v.quantization}")
        print(f"Input {k}: {v.shape}")
    for k, v in inf_service.outputs.items():
        print(f"Output {k}: {v.dtype}")
        print(f"Output {k}: {v.format}")
        print(f"Output {k}: {v.height}")
        print(f"Output {k}: {v.width}")
        print(f"Output {k}: {v.key}")
        print(f"Output {k}: {v.location}")
        print(f"Output {k}: {v.name}")
        print(f"Output {k}: {v.quantization}")
        print(f"Output {k}: {v.shape}")


if __name__ == "__main__":
    opt = parse_opt()
    result_file_path = main(opt.model_file_path, opt.dataset_file_path)