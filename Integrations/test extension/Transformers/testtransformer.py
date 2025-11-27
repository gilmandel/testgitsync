from SiemplifyTransformer import SiemplifyTransformer

def main():
    transformer = SiemplifyTransformer()

    transformer_input_param = transformer.extract_param("input")
    # Get extra parameters if needed
    # e.g. param_x = transformer.extract_param("param_x")
    
    # Add custom transformer logic here 
    result = f"transformed {transformer_input_param}" # Set the transformer result
   
    transformer.LOGGER.info("finished executing the transformer")
    transformer.end(result)


if __name__ == "__main__":
    main()
