async function generatePrompt() {
    const taskInput = document.getElementById('taskInput').value;
    const modelType = document.getElementById('modelType').value;
    const promptOutput = document.getElementById('promptOutput');
    
    if (!taskInput.trim()) {
        alert('请输入任务描述');
        return;
    }

    // 显示加载动画
    document.getElementById('loading').style.display = 'flex';
    // 添加生成中的样式
    promptOutput.classList.add('generating');

    try {
        // 根据选择的模型类型调用不同的接口
        let endpoint;
        switch(modelType) {
            case 'openai':
                endpoint = '/api/v1/yj/promptgen/openai';
                break;
            case 'claude':
                endpoint = '/api/v1/yj/promptgen/claude';
                break;
            case 'deepseek':
                endpoint = '/api/v1/yj/promptgen/deepseek';
                break;
            default:
                throw new Error('未知的模型类型');
        }

        const response = await fetch(endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 
                task: taskInput,
                variable: [''] // 添加 variable 参数，用于 Claude 接口
            })
        });

        const data = await response.json();
        promptOutput.value = data.prompt;
    } catch (error) {
        alert('生成失败: ' + error.message);
    } finally {
        // 隐藏加载动画
        document.getElementById('loading').style.display = 'none';
        // 移除生成中的样式
        promptOutput.classList.remove('generating');
        // 聚焦到输出框，方便用户直接编辑
        promptOutput.focus();
    }
}

function clearTask() {
    document.getElementById('taskInput').value = '';
    document.getElementById('taskInput').focus();
}

function copyToClipboard() {
    const promptOutput = document.getElementById('promptOutput');
    promptOutput.select();
    document.execCommand('copy');
    
    // 显示复制成功提示
    const toast = document.getElementById('copyToast');
    toast.classList.add('show');
    setTimeout(() => {
        toast.classList.remove('show');
    }, 2000);
}