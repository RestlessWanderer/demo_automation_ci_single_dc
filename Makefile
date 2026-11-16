.PHONY: help
help: ## Display help message
	@grep -E '^[0-9a-zA-Z_-]+\.*[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: build-dc1
build-dc1: ## Build Production and Digital Twin Configs
	ansible-playbook playbooks/build_dt.yml -i sites/dc1/inventory_act.yml -e "target_fabric=dc1"
	ansible-playbook playbooks/build.yml -i sites/dc1/inventory.yml -e "target_fabric=dc1"

.PHONY: deploy-dc1
deploy-dc1: ## Deploy Configs
	ansible-playbook playbooks/deploy.yml -i sites/dc1/inventory.yml -e "target_fabric=dc1"

.PHONY: validate-dc1
validate-dc1: ## Validate Configs
	ansible-playbook playbooks/validate.yml -i sites/dc1/inventory.yml -e "target_fabric=dc1"

.PHONY: build-dc1_dt
build-dc1_dt: ## Build Configs - DT
	ansible-playbook playbooks/build_dt.yml -i sites/dc1/inventory.yml -e "target_fabric=dc1"

.PHONY: deploy-dc1_dt
deploy-dc1_dt: ## Deploy Configs - DT
	ansible-playbook playbooks/deploy_dt.yml -i sites/dc1/inventory_act.yml -e "target_fabric=dc1"

.PHONY: validate-dc1_dt
validate-dc1_dt: ## Validate Configs - DT
	ansible-playbook playbooks/validate_dt.yml -i sites/dc1/inventory_act.yml -e "target_fabric=dc1"