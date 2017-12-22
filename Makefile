include env/utils/colors.sh

.PHONY: dev
dev:
	@echo "${CYAN}-> Stopping environment ${NC}"
	docker-compose down
	docker-compose rm -vf
	@echo "${CYAN}-> Rebuilding environments ${NC}"
	docker-compose build
	@echo "${GREEN}-> Starting -= DEV =- environment ${NC}"
	docker-compose up
