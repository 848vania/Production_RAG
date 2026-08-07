from dataclasses import dataclass
from pathlib import Path
import yaml 


@dataclass
class RetrievalConfig:
    type: str
    top_k: int
    vector_top_k: int
    keyword_top_k: int 
    vector_weight: float
    keyword_weight: float 


@dataclass
class RerankerConfig:
    enabled: bool
    top_k: int 


@dataclass
class GenerationConfig:
    provider: str 
    model: str 


@dataclass
class ExperimentConfig:
    name: str 
    retrieval: RetrievalConfig
    reranker: RerankerConfig
    generation: GenerationConfig
    config_path: str


def load_experiment_config(config_path: str) -> ExperimentConfig:
    """
    Load one YAML experiment config file
    """
    path = Path(config_path)

    with path.open('r', encoding= 'utf-8') as file:
        raw_config = yaml.safe_load(file)

    retrieval = raw_config['retrieval']
    reranker = raw_config['reranker']
    generation = raw_config['generation']

    return ExperimentConfig(
        name = raw_config['name'],
        retrieval = RetrievalConfig(
            type = retrieval['type'],
            top_k = retrieval['top_k'],
            vector_top_k= retrieval['vector_top_k'],
            keyword_top_k= retrieval['keyword_top_k'],
            vector_weight= retrieval['vector_weight'],
            keyword_weight= retrieval['keyword_weight'],
        ),
        reranker= RerankerConfig(
            enabled= reranker['enabled'],
            top_k = reranker['top_k'],
        ),
        generation= GenerationConfig(
            provider= generation['provider'],
            model = generation['model'],
        ),
        config_path= str(path),
    )


def load_experiment_configs(config_paths: list[str]) -> list[ExperimentConfig]:
    """
    Load multiple experiment config files
    """
    return [load_experiment_config(config_path) for config_path in config_paths]


def experiment_config_to_dict(config: ExperimentConfig) -> dict:
    """
    Convert config dataclass into serializable dictionary
    """
    return {
        'name': config.name,
        'config_path': config.config_path,
        'retrieval': {
            'type': config.retrieval.type,
            'top_k': config.retrieval.top_k,
            'vector_top_k': config.retrieval.vector_top_k,
            'keyword_top_k': config.retrieval.keyword_top_k,
            'vector_weight': config.retrieval.vector_weight,
            'keyword_weight': config.retrieval.keyword_weight,
        },
        'reranker': {
            'enabled': config.reranker.enabled,
            'top_k': config.reranker.top_k,
        },
        'generation': {
            'provider': config.generation.provider,
            'model': config.generation.model,
        },
    }