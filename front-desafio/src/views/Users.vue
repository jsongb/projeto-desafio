<template>
    <!-- Tela de listagem dos usuários -->
    <div>
        <b-row class="justify-content-md-center">
            <b-col md="8">
                <!-- Formulário de busca -->
                <form @submit.prevent="requestUsers" class="input-search">

                    <!-- Campo de busca por texto -->
                    <b-form-input v-model="search" class="m-1" id="search" placeholder="Buscar" size="lg"/>

                    <!-- Botão submit para buscar -->
                    <b-btn type="submit" class="m-1" variant="primary" size="lg" :title="'Clique para buscar'">
                        <b-icon-search/>
                    </b-btn>

                    <!-- Botão de limpar a busca -->   
                    <b-btn class="m-1" variant="warning" size="lg" :title="'Clique para limpar a busca'" @click="clearFilter">
                        <b-icon-eraser/>
                    </b-btn>

                    <!-- Botão para adicionar um novo registro -->
                    <b-btn class="m-1" variant="success" size="lg" :title="'Clique para cadastrar'" @click="openUserModal(null)">
                        <b-icon-plus/>
                    </b-btn>
                </form>
            </b-col>
        </b-row>
        <b-row class="justify-content-md-center mt-4">
            <b-col md="8">

                <!-- Tabela responsiva para listagem dos usuários -->
                <b-table responsive striped hover :items="users" :fields="fields">
                    
                    <!-- Campo customizado na tabela para exibir a senha de forma abreviada -->
                    <template #cell(password)="data">
                        <b :title="data.item.password">
                            {{ data.item.password.substr(0,15) }}...
                        </b>
                    </template>
                    
                    <!-- Campo customizado na tabela para exibir os botões de ação (Editar e Remover) -->
                    <template #cell(actions)="data">
                        <b-row>
                            <b-col>
                                <b-btn variant="primary" class="m-1" @click="openUserModal(data.item.register)" :title="'Clique para editar'">
                                    <b-icon-pen/>
                                </b-btn>
                                <b-btn variant="outline-danger" class="m-1" :title="'Clique para excluir'" @click="deleteUser(data.item.register)">
                                    <b-icon-trash/>
                                </b-btn>
                            </b-col>
                        </b-row>
                    </template>
                </b-table>
            </b-col>
        </b-row>

        <!-- Componente de modal para criação/edição de usuário -->
        <UserForm @refresh="requestUsers()"/>

        <!-- Componente de modal para exclusão de usuário -->
        <DeleteUser @refresh="requestUsers()"/>
    </div>
</template>

<script>
    // Método de requisição usando biblioteca Axios (importado de /src/utils/request.js)
    import request from '@/utils/request'

    //Importando componentes
    import UserForm from '@/components/UserForm'
    import DeleteUser from '@/components/DeleteUser'


    export default {
        // Componentes usados nessa tela
        components:{
            UserForm,
            DeleteUser
        },

        // Método de montagem, executado na abertura da página
        mounted(){

            // Executando método de requisição dos usuários
            this.requestUsers()
        },

        // Dados usados nessa tela
        data() {
            return {
                // Variável para formulário de filtro e busca
                search: '',

                // Lista de usuários
                users: [],

                // Campos da tabela
                fields: [
                    {
                        key: 'name',
                        label: 'Nome',
                    },
                    {
                        key: 'born_date',
                        label: 'Data de nascimento',
                    },
                    {
                        key: 'email',
                        label: 'E-mail',
                    },
                    {
                        key: 'password',
                        label: 'Senha',
                    },
                    {
                        key: 'register',
                        label: 'Matrícula',
                    },
                    {
                        key: 'actions',
                        label: 'Ações',
                    }
                ],
            }
        },

        // Métodos usados nessa tela
        methods: {

            // Método de requisição dos usuários
            requestUsers(){

                // Fazendo requisição dos usuários na API
                request(
                    `api/user/?search=${this.search}`,
                    'GET',
                    {},
                    (r)=>{
                        this.users = []

                        // Populando lista de usuários com os dados da API
                        r.data.forEach(user => {
                            this.users.push({
                                name: user.name,
                                born_date: new Date(user.born_date).toLocaleDateString(),
                                email: user.email,
                                password: user.password,
                                register: user.register,
                            })
                        })
                    }
                )
            },

            // Método para abrir o modal com formulário do usuário
            // Ao passar o ID por parâmetro é considerado uma edição do usuário
            openUserModal(user = null){
                this.$store.state.current_user = user
                this.$bvModal.show('user')
            },

            // Método para abrir o modal de exclusão do usuário
            deleteUser(user){
                this.$store.state.current_user = user
                this.$bvModal.show('delete-user')
            },

            // Método para limpar os filtros na busca
            clearFilter(){
                this.search = ''
                this.requestUsers()
            },
        }
    }
</script>

<style>
    .input-search{
        max-width: 100%;
        display: flex;
    }
</style>