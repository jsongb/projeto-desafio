<template>
    <!-- Formulário do usuário -->
    <div>
        <b-modal id="user" hide-footer title="Dados do usuário" hide-header-close size="lg" no-close-on-esc no-close-on-backdrop @show="getUser">
            <b-row>
                <b-col>
                    <form @submit.prevent="saveUser">
                        <b-row>
                            <!-- Campo nome -->
                            <b-col md="7">
                                <label for="user-name">
                                    Nome
                                </label>
                                <b-form-input id="user-name" v-model="user.name" required/>
                            </b-col>

                            <!-- Campo de e-mail -->
                            <b-col md="5">
                                <label for="user-email">
                                    E-mail
                                </label>
                                <b-form-input type="email" id="user-email" v-model="user.email" required/>
                            </b-col>

                            <!-- Campo de data de nascimento -->
                            <b-col md="4">
                                <label for="user-born">
                                    Data de nascimento
                                </label>
                                <b-form-input type="date" id="user-born" v-model="user.born_date" required/>
                            </b-col>

                            <!-- Campo de senha -->
                            <b-col md="4">
                                <label for="user-password">
                                    Senha
                                </label>
                                <b-form-input type="password" id="user-password" v-model="user.password" required/>
                            </b-col>

                            <!-- Campo de confirmação de senha -->
                            <b-col md="4">
                                <label for="user-password2">
                                    Confirmação de senha
                                </label>
                                <b-form-input type="password" id="user-password2" v-model="user.password2" required/>
                            </b-col>
                        </b-row>
                        <hr>
                        <b-row>
                            <!-- Botão cancelar -->
                            <b-col md="6">
                                <b-btn class="m-1 w-100" v-b-popover.hover.bottom="'Cancelar'" variant="outline-danger" @click="closeUser">
                                    <b-icon-x/> Cancelar
                                </b-btn>
                            </b-col>

                            <!-- Botão de salvar -->
                            <b-col md="6">
                                <b-btn class="m-1 w-100" v-b-popover.hover.bottom="'Salvar'" variant="success" type="submit">
                                    <b-icon-check2-circle/> Salvar
                                </b-btn>
                            </b-col>
                        </b-row>
                    </form>
                </b-col>
            </b-row>
        </b-modal>
    </div>
</template>

<script>
    // Importando biblioteca
    import request from '@/utils/request'
    import Alert from '@/utils/Alert'

    export default {
        // Definindo propriedade para recarregar a lista de usuários após a exclusão
        props: ['refresh'],
        
        // Dados usados nessa tela
        data(){
            return {
                user: {
                    name: '',
                    born_date: '',
                    email: '',
                    password: '',
                    password2: '',
                },
            }
        },

        // Métodos usados nessa tela
        methods: {

            // Função responsável por fazer a requisição dos dados do usuário na abertura do modal
            // Caso não haja ID definido, o formulário abre vazio (para cadastro)
            getUser(){
                if(!this.$store.state.current_user){
                    this.resetForm()
                    return
                }

                request(
                    this.getUserEndpoint(),
                    'GET',
                    {},
                    (r)=>{
                        this.user = {
                            name: r.data.name,
                            born_date: r.data.born_date,
                            email: r.data.email,
                        }
                    },
                    (error)=>{
                        Alert(
                            'Desculpe, não foi possível obter dados do usuário',
                            'd'
                        )
                    }
                )
            },

            // Função responsável por salvar os dados do usuário na api
            saveUser(){
                if(!this.passwordValidation()){
                    return
                }
                if(!this.dateValidation()){
                    return
                }
                request(
                    this.getUserEndpoint(),
                    this.$store.state.current_user?'PUT':'POST',
                    this.user,
                    (r)=>{
                        Alert(
                            'Usuário cadastrado/atualizado',
                            's'
                        )
                        this.closeUser()
                    },
                    (error)=>{
                        Alert(
                            `Desculpe, verifique se os campos foram preenchidos corretamente ${!this.$store.state.current_user?'ou se o e-mail já foi cadastrado.':''}`,
                            'w'
                        )
                    }
                )
            },

            // Função responsável por montar o endereço da URL do usuário caso haja ID
            getUserEndpoint(){
                let endpoint = `api/user/`

                if(this.$store.state.current_user){
                    endpoint = `${endpoint}${this.$store.state.current_user}/`
                }

                return endpoint
            },

            // Função reponsável por fechar o formulário do usuário
            closeUser(){
                this.$bvModal.hide('user')
                this.$emit('refresh')
                this.$store.state.current_user = null
            },

            // Função responsável por validar a data de nascimento
            dateValidation(){
                let date = new Date(this.user.born_date)

                if(date.getFullYear() <= 999 || date.getFullYear() > 9999){
                    Alert('Desculpe, digite uma data válida', 'w')

                    return false
                }

                return true
            },

            // Função responsável por validar a senha
            passwordValidation(){
                if(this.user.password!=this.user.password2){
                    Alert(
                        'As senhas são diferentes',
                        'w'
                    )
                    return false
                }

                if(this.user.password.length < 8){
                    Alert(
                        'A senha precisa conter ao menos 8 digitos.',
                        'w'
                    )
                    return false
                }
                return true
            },

            // Função responsável por limpar os campos do formulário
            resetForm(){
                this.user = {
                    name: '',
                    born_date: '',
                    email: '',
                    password: '',
                    password2: '',
                }
            }
        }
    }
</script>